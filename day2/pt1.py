import csv
import argparse
from utils import ReportType, validate_report_simple


def count_safe_reports_pt1(input_file: str) -> int:

    answer = 0

    with open(input_file) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for row in csvreader:
            row = list(filter(None, row))
            int_row = [int(value) for value in row]
            if validate_report_simple(int_row) == ReportType.SAFE:
                answer += 1

    print(answer)
    return(answer)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count the number of safe reports in the input file.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    count_safe_reports_pt1(args.input_file)