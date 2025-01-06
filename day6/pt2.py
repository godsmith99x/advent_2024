import argparse
from utils import

def sum_middle_values_pt2(input_file: str) -> int:

    answer = 0

    with open(input_file, "r") as file:
        lines = file.readlines()
    

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count of the word xmas in a 2d grid.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    sum_middle_values_pt2(args.input_file)