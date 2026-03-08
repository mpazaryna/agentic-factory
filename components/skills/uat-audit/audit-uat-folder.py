# /// script
# requires-python = ">=3.11"
# ///
"""
UAT Folder Audit Script

Validates docs/uat/ against the spec in .claude/skills/uat-audit/spec.md.
Checks file naming (R1), format (R2), manifest coverage (R3), walkthrough
quality (R4 structural only), steps structure (R5 structural), directory
flatness (R6), and sync-map completeness (R7).

Usage:
    uv run .claude/skills/uat-audit/audit-uat-folder.py [OPTIONS]

Options:
    --all           Run all checks (default)
    --naming        R1: File naming validation
    --format-check  R2: Section structure validation
    --coverage      R3: Manifest bidirectional coverage
    --sync-map      R7: .sync-map.json validation
    --json          Output machine-readable JSON
    --fix           Auto-fix structural issues (rename, sort manifest)
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).resolve().parents[3]  # .claude/skills/uat-audit -> repo root
UAT_DIR = REPO_ROOT / "docs" / "uat"
MANIFEST_PATH = REPO_ROOT / "docs" / "guides" / "manifest.json"
SYNC_MAP_PATH = UAT_DIR / ".sync-map.json"

# R1: filename pattern — {3-4 digit id}-{kebab-case slug}.md
# Also allows sub-IDs like 302-02 (id-subid-slug.md)
FILENAME_RE = re.compile(r"^(\d{3,4}(?:-\d{2})?)-([a-z0-9]+(?:-[a-z0-9]+)*)\.md$")

# R2: required heading pattern
HEADING_RE = re.compile(r"^#\s+(\d{3,4}(?:-\d{2})?)\s*\u2014\s*(.+)$")

# R2: allowed sections in order
ALLOWED_SECTIONS = ["Walkthrough", "Steps", "Notes"]

# Files to skip (not UAT test cases)
SKIP_FILES = {"README.md", "index.json"}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class Violation:
    rule: str
    file: str
    message: str
    fixable: bool = False


@dataclass
class AuditReport:
    violations: list[Violation] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def add(self, rule: str, file: str, message: str, *, fixable: bool = False):
        self.violations.append(Violation(rule, file, message, fixable))

    @property
    def passed(self) -> bool:
        return len(self.violations) == 0

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "violation_count": len(self.violations),
            "stats": self.stats,
            "violations": [
                {"rule": v.rule, "file": v.file, "message": v.message, "fixable": v.fixable}
                for v in self.violations
            ],
        }

    def print_text(self):
        if self.passed:
            print(f"\n  ALL CHECKS PASSED  ({self.stats.get('total_files', 0)} files audited)\n")
            return

        print(f"\n  AUDIT FAILED  — {len(self.violations)} violation(s)\n")

        by_rule: dict[str, list[Violation]] = {}
        for v in self.violations:
            by_rule.setdefault(v.rule, []).append(v)

        for rule, violations in sorted(by_rule.items()):
            fixable_count = sum(1 for v in violations if v.fixable)
            fix_label = f" ({fixable_count} fixable)" if fixable_count else ""
            print(f"  [{rule}] — {len(violations)} violation(s){fix_label}")
            for v in violations:
                fix_marker = " [fixable]" if v.fixable else ""
                print(f"    - {v.file}: {v.message}{fix_marker}")
            print()

        if self.stats:
            print("  Stats:")
            for k, v in self.stats.items():
                print(f"    {k}: {v}")
            print()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_uat_files() -> list[Path]:
    """Return all .md files in docs/uat/ excluding skipped files."""
    if not UAT_DIR.exists():
        return []
    return sorted(
        p for p in UAT_DIR.glob("*.md")
        if p.name not in SKIP_FILES
    )


def extract_id_from_filename(name: str) -> str | None:
    """Extract the ID portion from a UAT filename."""
    m = FILENAME_RE.match(name)
    return m.group(1) if m else None


def parse_sections(text: str) -> list[tuple[str, str]]:
    """Parse markdown into (heading, content) tuples for ## headings."""
    sections = []
    current_heading = None
    current_lines: list[str] = []

    for line in text.split("\n"):
        if line.startswith("## "):
            if current_heading is not None:
                sections.append((current_heading, "\n".join(current_lines).strip()))
            current_heading = line[3:].strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections.append((current_heading, "\n".join(current_lines).strip()))

    return sections


def word_count(text: str) -> int:
    """Count words in text, ignoring markdown image syntax."""
    cleaned = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    return len(cleaned.split())


def load_manifest() -> dict | None:
    """Load and return manifest.json, or None if invalid."""
    try:
        return json.loads(MANIFEST_PATH.read_text())
    except (json.JSONDecodeError, FileNotFoundError):
        return None


def load_sync_map() -> dict | None:
    """Load and return .sync-map.json tasks dict, or None if invalid."""
    try:
        data = json.loads(SYNC_MAP_PATH.read_text())
        return data.get("tasks", data)
    except (json.JSONDecodeError, FileNotFoundError):
        return None


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_naming(report: AuditReport, files: list[Path]):
    """R1: File naming convention."""
    seen_ids: dict[str, str] = {}

    for f in files:
        m = FILENAME_RE.match(f.name)
        if not m:
            report.add("R1", f.name, f"Filename does not match pattern {{id}}-{{slug}}.md", fixable=True)
            continue

        file_id = m.group(1)

        # Check for duplicate IDs
        if file_id in seen_ids:
            report.add("R1", f.name, f"Duplicate ID {file_id} (also in {seen_ids[file_id]})")
        else:
            seen_ids[file_id] = f.name


def check_format(report: AuditReport, files: list[Path]):
    """R2: Gold-standard file format."""
    for f in files:
        # Skip files that already failed naming (can't parse ID)
        file_id = extract_id_from_filename(f.name)
        if file_id is None:
            continue

        text = f.read_text()
        lines = text.split("\n")

        # Check H1 heading
        if not lines or not lines[0].strip():
            report.add("R2", f.name, "File is empty or does not start with H1 heading")
            continue

        h1_match = HEADING_RE.match(lines[0].strip())
        if not h1_match:
            report.add("R2", f.name, f"H1 heading must be '# {{id}} \\u2014 {{Title}}' (em dash required), got: {lines[0][:60]}", fixable=True)
        elif h1_match.group(1) != file_id:
            report.add("R2", f.name, f"H1 ID '{h1_match.group(1)}' does not match filename ID '{file_id}'", fixable=True)

        # Check sections
        sections = parse_sections(text)
        section_names = [name for name, _ in sections]

        # Check for forbidden sections
        forbidden = {"Results", "Expected Results"}
        for name in section_names:
            if name in forbidden:
                report.add("R2", f.name, f"Forbidden section '## {name}' found")

        # Check for metadata block (lines like "Priority:", "Status:" before first ##)
        pre_section = text.split("## ")[0] if "## " in text else text
        metadata_re = re.compile(r"^\*?\*?(Priority|Status|Last Updated|ClickUp)\*?\*?\s*:", re.MULTILINE)
        if metadata_re.search(pre_section):
            report.add("R2", f.name, "Metadata block found (Priority/Status/etc.) — remove it", fixable=True)

        # Check required sections exist
        if "Walkthrough" not in section_names:
            report.add("R2", f.name, "Missing required '## Walkthrough' section")
        if "Steps" not in section_names:
            report.add("R2", f.name, "Missing required '## Steps' section")

        # Check section ordering
        allowed_indices = {name: i for i, name in enumerate(ALLOWED_SECTIONS)}
        prev_idx = -1
        for name in section_names:
            if name in allowed_indices:
                idx = allowed_indices[name]
                if idx < prev_idx:
                    report.add("R2", f.name, f"Section '## {name}' is out of order (must be: Walkthrough, Steps, Notes)")
                    break
                prev_idx = idx
            elif name not in forbidden:
                report.add("R2", f.name, f"Unknown section '## {name}' — only Walkthrough, Steps, Notes allowed")


def check_walkthrough(report: AuditReport, files: list[Path]):
    """R4: Walkthrough content quality (structural checks only)."""
    for f in files:
        if extract_id_from_filename(f.name) is None:
            continue

        text = f.read_text()
        sections = dict(parse_sections(text))

        walkthrough = sections.get("Walkthrough", "")
        if not walkthrough:
            continue  # Already flagged by R2

        wc = word_count(walkthrough)
        if wc < 100:
            report.add("R4", f.name, f"Walkthrough is {wc} words (minimum 100)")
        elif wc > 1000:
            report.add("R4", f.name, f"Walkthrough is {wc} words (maximum 1000)")

        # Check for cross-references to other UAT files
        if re.search(r"\d{3,4}-[a-z].*\.md", walkthrough):
            report.add("R4", f.name, "Walkthrough cross-references another UAT file (too brittle)")


def check_steps(report: AuditReport, files: list[Path]):
    """R5: Steps section structure (structural checks only)."""
    for f in files:
        if extract_id_from_filename(f.name) is None:
            continue

        text = f.read_text()
        sections = dict(parse_sections(text))

        steps = sections.get("Steps", "")
        if not steps:
            continue  # Already flagged by R2

        # Check that steps contain numbered items
        has_numbered = bool(re.search(r"^\d+[\.\)]\s", steps, re.MULTILINE))
        has_scenario_numbered = bool(re.search(r"^\d+[A-Z][\.\)]\s", steps, re.MULTILINE))
        if not has_numbered and not has_scenario_numbered:
            report.add("R5", f.name, "Steps section has no numbered items")


def check_coverage(report: AuditReport, files: list[Path]):
    """R3: Manifest bidirectional coverage."""
    manifest = load_manifest()
    if manifest is None:
        report.add("R3", "manifest.json", "Cannot load or parse docs/guides/manifest.json")
        return

    # Collect all IDs from manifest
    manifest_ids: set[str] = set()
    for guide in manifest.get("guides", []):
        for id_ in guide.get("ids", []):
            manifest_ids.add(id_)

    # Collect all IDs from files
    file_ids: set[str] = set()
    for f in files:
        fid = extract_id_from_filename(f.name)
        if fid:
            file_ids.add(fid)

    # Files not in manifest
    orphaned = file_ids - manifest_ids
    for fid in sorted(orphaned):
        report.add("R3", f"{fid}-*.md", f"ID {fid} exists on disk but is not in any guide in manifest.json", fixable=True)

    # Manifest IDs without files
    stale = manifest_ids - file_ids
    for fid in sorted(stale):
        report.add("R3", "manifest.json", f"ID {fid} is in manifest but no matching file exists on disk")

    # Duplicate IDs within a single guide
    for guide in manifest.get("guides", []):
        ids = guide.get("ids", [])
        seen = set()
        for id_ in ids:
            if id_ in seen:
                report.add("R3", "manifest.json", f"Duplicate ID {id_} in guide '{guide['name']}'")
            seen.add(id_)

    report.stats["manifest_ids"] = len(manifest_ids)
    report.stats["file_ids"] = len(file_ids)
    report.stats["orphaned"] = len(orphaned)
    report.stats["stale"] = len(stale)


def check_directory(report: AuditReport):
    """R6: Directory structure (flat, no subdirs)."""
    if not UAT_DIR.exists():
        report.add("R6", "docs/uat/", "Directory does not exist")
        return

    for item in UAT_DIR.iterdir():
        if item.is_dir():
            report.add("R6", item.name, f"Subdirectory found in docs/uat/ — must be flat")

    # Check for non-md, non-json files
    for item in UAT_DIR.iterdir():
        if item.is_file() and not item.name.endswith((".md", ".json")):
            report.add("R6", item.name, f"Unexpected file type in docs/uat/ — only .md and .json allowed")


def check_sync_map(report: AuditReport, files: list[Path]):
    """R7: .sync-map.json validation."""
    if not SYNC_MAP_PATH.exists():
        report.add("R7", ".sync-map.json", "File does not exist")
        return

    tasks = load_sync_map()
    if tasks is None:
        report.add("R7", ".sync-map.json", "Cannot load or parse .sync-map.json")
        return

    sync_ids = set(tasks.keys())
    file_ids: set[str] = set()
    for f in files:
        fid = extract_id_from_filename(f.name)
        if fid:
            file_ids.add(fid)

    missing_from_sync = file_ids - sync_ids
    for fid in sorted(missing_from_sync):
        report.add("R7", ".sync-map.json", f"ID {fid} has a UAT file but no entry in .sync-map.json", fixable=True)

    report.stats["sync_map_ids"] = len(sync_ids)
    report.stats["missing_from_sync_map"] = len(missing_from_sync)


# ---------------------------------------------------------------------------
# Fix mode
# ---------------------------------------------------------------------------

def apply_fixes(report: AuditReport):
    """Apply auto-fixes for fixable violations. Returns count of fixes applied."""
    fixes = 0
    # For now, only report what would be fixed. Actual fix logic can be
    # expanded as the spec matures. The agent layer handles complex fixes.
    fixable = [v for v in report.violations if v.fixable]
    if fixable:
        print(f"\n  {len(fixable)} fixable violation(s) detected.")
        print("  Use the uat-audit skill with an agent to auto-remediate.\n")
    return fixes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = set(sys.argv[1:])

    output_json = "--json" in args
    do_fix = "--fix" in args
    args.discard("--json")
    args.discard("--fix")

    # Default to --all if no specific checks requested
    run_all = "--all" in args or not (args & {"--naming", "--format-check", "--coverage", "--sync-map"})

    report = AuditReport()
    files = get_uat_files()
    report.stats["total_files"] = len(files)

    if run_all or "--naming" in args:
        check_naming(report, files)

    if run_all or "--format-check" in args:
        check_format(report, files)
        check_walkthrough(report, files)
        check_steps(report, files)

    if run_all or "--coverage" in args:
        check_coverage(report, files)

    if run_all:
        check_directory(report)

    if run_all or "--sync-map" in args:
        check_sync_map(report, files)

    if do_fix:
        apply_fixes(report)

    if output_json:
        print(json.dumps(report.to_dict(), indent=2))
    else:
        report.print_text()

    sys.exit(0 if report.passed else 1)


if __name__ == "__main__":
    main()
