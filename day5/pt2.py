import argparse
from utils import get_rules, correct_order, sort_pages, median_page_num

def sum_middle_values_pt2(input_file: str) -> int:

    answer = 0

    with open(input_file, "r") as file:
        lines = file.readlines()
    
    rules = get_rules(lines)

    for line in lines:
        if "|" not in line and "," in line:
            page_list = line.split(",")
            if not correct_order(rules, page_list):
                answer += median_page_num(sort_pages(rules, page_list))

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count of the word xmas in a 2d grid.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    sum_middle_values_pt2(args.input_file)