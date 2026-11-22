#!/usr/bin/env python3
"""Contribution report from local git history (no GitHub API needed).

Usage:
    python scripts/contribution_report.py                 # print a table
    python scripts/contribution_report.py --md            # write docs/CONTRIBUTIONS.md
    python scripts/contribution_report.py --code-only     # count only src/ and tests/

Authors are grouped by name/email via .mailmap if you add one (see docs/GITHUB_SETUP.md).
Counts are a rough signal of activity, not a measure of effort or quality. Do not use them as grades.
"""
from __future__ import annotations

import argparse
import collections
import subprocess
from pathlib import Path


def git_log() -> str:
    return subprocess.run(
        ["git", "log", "--no-merges", "--numstat", "--format=@@%aN|%aE|%aI"],
        capture_output=True, text=True, check=True,
    ).stdout


def module_of(path: str) -> str:
    parts = path.split("/")
    if parts[:2] == ["src", "threat_detection"] and len(parts) > 3:
        return parts[2]
    return parts[0] if len(parts) > 1 else "(root)"


def collect(code_only: bool):
    authors = collections.defaultdict(lambda: {"commits": 0, "added": 0, "deleted": 0, "first": None, "last": None,
                                               "modules": collections.Counter()})
    current = None
    for line in git_log().splitlines():
        if line.startswith("@@"):
            name, _email, date = line[2:].split("|", 2)
            current = authors[name]
            current["commits"] += 1
            day = date[:10]
            current["first"] = min(filter(None, [current["first"], day]))
            current["last"] = max(filter(None, [current["last"], day]))
        elif line.strip() and current is not None:
            added, deleted, path = line.split("\t", 2)
            if added == "-" or deleted == "-":
                continue  # binary file
            if code_only and not path.startswith(("src/", "tests/")):
                continue
            current["added"] += int(added)
            current["deleted"] += int(deleted)
            current["modules"][module_of(path)] += int(added) + int(deleted)
    return authors


def render(authors) -> str:
    rows = ["| Author | Commits | Lines added | Lines removed | First | Last | Most-touched modules |",
            "|---|---|---|---|---|---|---|"]
    for name, a in sorted(authors.items(), key=lambda kv: -kv[1]["commits"]):
        top = ", ".join(m for m, _ in a["modules"].most_common(3)) or "-"
        rows.append(f"| {name} | {a['commits']} | {a['added']} | {a['deleted']} | {a['first']} | {a['last']} | {top} |")
    rows.append("")
    rows.append("_Commit and line counts are rough activity signals, not effort or quality. "
                "Reviews, design work, data collection and testing do not show up here._")
    return "\n".join(rows)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--md", action="store_true", help="write docs/CONTRIBUTIONS.md")
    p.add_argument("--code-only", action="store_true", help="count only src/ and tests/")
    args = p.parse_args()
    table = render(collect(args.code_only))
    if args.md:
        out = Path("docs/CONTRIBUTIONS.md")
        out.write_text("# Contributions (generated)\n\nRun `python scripts/contribution_report.py --md` to refresh.\n\n"
                       + table + "\n")
        print(f"wrote {out}")
    else:
        print(table)


if __name__ == "__main__":
    main()
