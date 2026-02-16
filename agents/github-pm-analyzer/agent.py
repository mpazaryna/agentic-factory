"""
GitHub PM Analyzer Agent

Autonomous agent for analyzing GitHub repositories, issues, and commit activity.
Provides trend analysis, daily activity reports, and repository sync capabilities.
"""

import json
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add github-pm to path for imports
GITHUB_PM_PATH = Path.home() / "workspace" / "github-pm"
sys.path.insert(0, str(GITHUB_PM_PATH / "src"))  # for github_pm package
sys.path.insert(0, str(GITHUB_PM_PATH))  # for scripts/workflows


class GitHubPMAgent:
    """
    Autonomous agent for GitHub project management analysis.

    Capabilities:
    - Trend analysis: Compare issue snapshots across time periods
    - Daily activity: Analyze commits across multiple repositories
    - Repository sync: Discover and filter repositories from GitHub
    """

    def __init__(self):
        """Initialize the GitHub PM analyzer agent."""
        self.github_pm_path = GITHUB_PM_PATH
        self.data_path = self.github_pm_path / "data"
        self.config_path = self.github_pm_path / "config"

    def execute(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute the requested analysis task.

        Args:
            config: Task configuration with 'task' key specifying the operation:
                - task: "trend_analysis" | "daily_activity" | "sync_repos" | "list_snapshots"
                - Additional task-specific parameters

        Returns:
            Dict with status, results, and any generated reports
        """
        task = config.get("task")

        if task == "trend_analysis":
            return self._analyze_trends(config)
        elif task == "daily_activity":
            return self._get_daily_activity(config)
        elif task == "sync_repos":
            return self._sync_repos(config)
        elif task == "list_snapshots":
            return self._list_snapshots()
        else:
            return {
                "status": "error",
                "message": f"Unknown task: {task}. Valid tasks: trend_analysis, daily_activity, sync_repos, list_snapshots"
            }

    def _analyze_trends(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Compare two issue snapshots to identify trends."""
        baseline_snapshot = config.get("baseline_snapshot")
        current_snapshot = config.get("current_snapshot")

        if not baseline_snapshot or not current_snapshot:
            return {
                "status": "error",
                "message": "Both baseline_snapshot and current_snapshot are required"
            }

        baseline_path = self.data_path / baseline_snapshot / "raw.json"
        current_path = self.data_path / current_snapshot / "raw.json"

        if not baseline_path.exists():
            return {"status": "error", "message": f"Baseline snapshot not found: {baseline_snapshot}"}
        if not current_path.exists():
            return {"status": "error", "message": f"Current snapshot not found: {current_snapshot}"}

        try:
            # Import the comparator
            sys.path.insert(0, str(self.github_pm_path / "workflows" / "trend_analysis"))
            from compare_periods import PeriodComparator

            with open(baseline_path) as f:
                baseline = json.load(f)
            with open(current_path) as f:
                current = json.load(f)

            comparator = PeriodComparator()
            results = comparator.compare(baseline, current)
            report = comparator.generate_report(results)

            return {
                "status": "success",
                "task": "trend_analysis",
                "baseline_snapshot": baseline_snapshot,
                "current_snapshot": current_snapshot,
                "insights": results["insights"],
                "overall_changes": results["overall_changes"],
                "state_changes": results["state_changes"],
                "repository_changes": results["repository_changes"],
                "report": report
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _get_daily_activity(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Generate multi-repo daily/weekly activity report."""
        days = config.get("days", 7)
        config_file = config.get("config_file", "config/collection/production.yaml")

        try:
            # Import the generator
            sys.path.insert(0, str(self.github_pm_path / "workflows" / "code_analysis"))
            from daily_activity import DailyActivityReportGenerator

            generator = DailyActivityReportGenerator()
            config_path = str(self.github_pm_path / config_file)

            data = generator.generate_report(config_path, days, "markdown")

            return {
                "status": "success",
                "task": "daily_activity",
                "days": days,
                "metadata": data["metadata"],
                "totals": data["totals"],
                "repositories": list(data["repositories"].keys()),
                "report": data.get("markdown", "")
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _sync_repos(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """Sync repositories from GitHub and apply filters."""
        dry_run = config.get("dry_run", True)
        filters_file = config.get("filters_file", "config/collection/repo_filters.yaml")

        try:
            # Import the syncer
            sys.path.insert(0, str(self.github_pm_path / "scripts"))
            from sync_repos import RepoSyncer

            filters_path = self.github_pm_path / filters_file
            syncer = RepoSyncer(filters_path)
            repo_config, stats = syncer.sync()

            result = {
                "status": "success",
                "task": "sync_repos",
                "dry_run": dry_run,
                "stats": stats,
                "repositories": repo_config.get("repositories", [])
            }

            if not dry_run:
                # Write the config
                output_path = self.github_pm_path / "config" / "collection" / "production.yaml"
                import yaml
                with open(output_path, "w") as f:
                    f.write("# Auto-generated by github-pm-analyzer agent\n")
                    f.write(f"# Generated: {datetime.now().isoformat()}\n\n")
                    yaml.dump(repo_config, f, default_flow_style=False, sort_keys=False)
                result["output_file"] = str(output_path)

            return result
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _list_snapshots(self) -> Dict[str, Any]:
        """List available issue data snapshots."""
        if not self.data_path.exists():
            return {"status": "error", "message": "Data directory not found"}

        snapshots = sorted([
            d.name for d in self.data_path.iterdir()
            if d.is_dir() and (d / "raw.json").exists()
        ], reverse=True)

        return {
            "status": "success",
            "task": "list_snapshots",
            "snapshots": snapshots,
            "total": len(snapshots)
        }


if __name__ == "__main__":
    # Test the agent
    agent = GitHubPMAgent()

    # Test list snapshots
    result = agent.execute({"task": "list_snapshots"})
    print(json.dumps(result, indent=2))
