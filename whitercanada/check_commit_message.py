#!/usr/bin/env python
import argparse
import re
from pathlib import Path

from whitercanada import get_config

COMMIT_PATTERN = re.compile(r"(.*?):(.*?)")


def check():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=Path, help="commit file")
    args = parser.parse_args()

    config = get_config("commit_msg")
    with open(args.file) as file:
        commit = file.read().strip().split("\n")[0]

    if config.get("allow_merge") and commit.startswith("Merge"):
        return 0

    if match := COMMIT_PATTERN.match(commit):
        prefixes = config.get("prefixes", [])
        if match[1] in prefixes:
            return 0
        else:
            print("Prefix should be in this list: ", ", ".join(prefixes))
            return 1
    else:
        print("Invalid commit message format")
        return 1


if __name__ == "__main__":
    exit(check())
