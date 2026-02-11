#!/usr/bin/env python3
"""Select, drop and reorder CSV columns by name."""

import argparse
import csv
import sys


def resolve(fieldnames, wanted, drop, ignore_missing=False):
    """Work out the output column order."""
    if wanted:
        missing = [c for c in wanted if c not in fieldnames]
        if missing and not ignore_missing:
            raise KeyError("no such column(s): %s" % ", ".join(missing))
        return [c for c in wanted if c in fieldnames]
    if drop:
        return [c for c in fieldnames if c not in drop]
    return list(fieldnames)


def cut(reader, columns):
    for row in reader:
        yield [row.get(c, "") for c in columns]


def split_list(value):
    return [part.strip() for part in value.split(",") if part.strip()]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("csv_file", help="path to the CSV file, or - for stdin")
    ap.add_argument("-f", "--fields", help="comma separated columns to keep, in order")
    ap.add_argument("-x", "--exclude", help="comma separated columns to drop")
    ap.add_argument("-d", "--delimiter", default=",", help="field delimiter")
    ap.add_argument("--ignore-missing", action="store_true",
                    help="skip requested columns that are not in the file")
    ap.add_argument("--list", action="store_true", help="just print the column names")
    args = ap.parse_args(argv)

    handle = sys.stdin if args.csv_file == "-" else open(args.csv_file, newline="", encoding="utf-8")
    try:
        reader = csv.DictReader(handle, delimiter=args.delimiter)
        if reader.fieldnames is None:
            return 0
        if args.list:
            for name in reader.fieldnames:
                print(name)
            return 0
        try:
            columns = resolve(reader.fieldnames, split_list(args.fields or ""),
                              split_list(args.exclude or ""), args.ignore_missing)
        except KeyError as exc:
            print("csvcut: %s" % exc.args[0], file=sys.stderr)
            return 2
        writer = csv.writer(sys.stdout, delimiter=args.delimiter, lineterminator="\n")
        writer.writerow(columns)
        writer.writerows(cut(reader, columns))
    finally:
        if handle is not sys.stdin:
            handle.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
