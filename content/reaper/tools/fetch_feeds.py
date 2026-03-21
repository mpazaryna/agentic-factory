#!/usr/bin/env python3
"""
Fetch RSS feeds from a URL, OPML file, or OPML XML string.

Usage:
    # Single feed
    python fetch_feeds.py https://blog.cloudflare.com/rss/

    # OPML file
    python fetch_feeds.py --opml ~/.feeds/tech.opml

    # OPML from stdin
    cat feeds.opml | python fetch_feeds.py --opml -

    # Limit entries per feed (default: 10)
    python fetch_feeds.py --opml ~/.feeds/tech.opml --limit 5

Output: JSON array of entries to stdout.
"""

import argparse
import json
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.request import urlopen, Request
from urllib.error import URLError


def fetch_feed(url, limit=10):
    """Fetch a single RSS/Atom feed and return entries."""
    try:
        req = Request(url, headers={"User-Agent": "kairos-reaper/1.0"})
        with urlopen(req, timeout=15) as resp:
            data = resp.read()
    except (URLError, TimeoutError) as e:
        return {"feed": url, "error": str(e), "entries": []}

    try:
        root = ET.fromstring(data)
    except ET.ParseError as e:
        return {"feed": url, "error": f"Parse error: {e}", "entries": []}

    # Detect RSS vs Atom
    entries = []
    feed_title = ""

    if root.tag == "rss" or root.find("channel") is not None:
        channel = root.find("channel")
        feed_title = (channel.findtext("title") or "").strip()
        for item in channel.findall("item")[:limit]:
            pub = item.findtext("pubDate") or ""
            try:
                pub_dt = parsedate_to_datetime(pub).isoformat() if pub else ""
            except (ValueError, TypeError):
                pub_dt = pub
            entries.append({
                "title": (item.findtext("title") or "").strip(),
                "link": (item.findtext("link") or "").strip(),
                "summary": (item.findtext("description") or "")[:500].strip(),
                "published": pub_dt,
            })
    else:
        # Atom
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        feed_title = (root.findtext("atom:title", "", ns) or root.findtext("title") or "").strip()
        for entry in root.findall("atom:entry", ns)[:limit]:
            if not entry:
                continue
            link_el = entry.find("atom:link[@rel='alternate']", ns)
            if link_el is None:
                link_el = entry.find("atom:link", ns)
            link = link_el.get("href", "") if link_el is not None else ""
            summary_el = entry.find("atom:summary", ns) or entry.find("atom:content", ns)
            summary = (summary_el.text or "")[:500].strip() if summary_el is not None else ""
            pub = entry.findtext("atom:published", "", ns) or entry.findtext("atom:updated", "", ns)
            entries.append({
                "title": (entry.findtext("atom:title", "", ns) or "").strip(),
                "link": link.strip(),
                "summary": summary,
                "published": pub.strip(),
            })

    return {"feed": url, "title": feed_title, "entries": entries}


def parse_opml(source):
    """Parse OPML and return list of feed URLs with metadata."""
    if source == "-":
        data = sys.stdin.read()
        root = ET.fromstring(data)
    else:
        root = ET.parse(source).getroot()

    feeds = []
    for outline in root.iter("outline"):
        xml_url = outline.get("xmlUrl")
        if xml_url:
            feeds.append({
                "url": xml_url,
                "title": outline.get("text") or outline.get("title") or "",
                "category": "",
            })
            # Walk up to find category
            parent = find_parent(root, outline)
            if parent is not None and parent.get("text"):
                feeds[-1]["category"] = parent.get("text")

    return feeds


def find_parent(root, target):
    """Find parent element of target in XML tree."""
    for parent in root.iter():
        for child in parent:
            if child is target:
                return parent
    return None


def main():
    parser = argparse.ArgumentParser(description="Fetch RSS feeds")
    parser.add_argument("url", nargs="?", help="Single feed URL")
    parser.add_argument("--opml", help="OPML file path (use - for stdin)")
    parser.add_argument("--limit", type=int, default=10, help="Max entries per feed")
    args = parser.parse_args()

    if not args.url and not args.opml:
        parser.print_help()
        sys.exit(1)

    results = []

    if args.opml:
        feeds = parse_opml(args.opml)
        for feed_info in feeds:
            result = fetch_feed(feed_info["url"], args.limit)
            result["category"] = feed_info.get("category", "")
            if not result.get("title"):
                result["title"] = feed_info.get("title", "")
            results.append(result)
    else:
        results.append(fetch_feed(args.url, args.limit))

    json.dump(results, sys.stdout, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
