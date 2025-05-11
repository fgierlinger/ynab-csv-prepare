#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,invalid-name
import csv
import datetime
from pathlib import Path
import re

REGEX = [re.compile(reg) for reg in [
    r"^Verwendungszweck: (?P<Payee>.+) Zahlungsreferenz: (?P<Memo>.+)$",
    r"^Zahlungsempfänger: (?P<Payee>.+) Verwendungszweck: (?P<Memo>.+)$",
    r"^Zahlungsreferenz: (?P<Payee>.{12})"
]]


def convert_csv(file: Path):
    """Convert Mein ELBA CSV file to ynab format.

    Args:
        file (Path): Path to Mein ELBA CSV
    """
    res = []
    with open(file, mode='rt', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile, delimiter=';')

        for row in reader:
            if len(row) < 6:
                continue  # Skip incomplete rows

            date1, _memo, _, amount, _, _ = row  # Ignore unwanted fields

            for pattern in REGEX:
                match = pattern.match(_memo)
                if match:
                    payee = match.group("Payee")
                    memo = match.group("Memo") if "Memo" in match.groupdict() else ""
                    if not memo:
                        memo = _memo
                    break
                else:
                    payee = ""
                    memo = _memo
            res.append([date1, payee, memo, amount])

    out_name = f"{file.parent}/ynab_{datetime.datetime.now().date()}.csv"
    with open(out_name, mode='wt', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerow(["Date", "Payee", "Memo", "Amount"])
        for row in res:
            writer.writerow(row)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('file', type=Path)

    args = parser.parse_args()
    convert_csv(args.file)
