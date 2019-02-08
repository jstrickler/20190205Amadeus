#!/usr/bin/env python
import sys
import fileinput

import argparse

parser = argparse.ArgumentParser(description="Faux Grep")

parser.add_argument("-i", action="store_true",
                    help="ignore case", dest="ignore_case")

parser.add_argument("pattern", help="pattern to find")

parser.add_argument("files", nargs="*", help="files to search (or STDIN)")

args = parser.parse_args()

if args.ignore_case:
    pattern = args.pattern.lower()
else:
    pattern = args.pattern

for line in fileinput.input(args.files):  # loop over sys.argv
    if args.ignore_case:
        line = line.lower()

    if pattern in line:
        print(line.rstrip())
