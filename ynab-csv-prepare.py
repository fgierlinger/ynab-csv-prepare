#!/usr/bin/env python3
# pylint: disable=missing-module-docstring,invalid-name
import csv
import datetime
from pathlib import Path


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

            date1, memo, _, amount, _, _ = row  # Ignore unwanted fields
            res.append([date1, "", memo, amount])

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
