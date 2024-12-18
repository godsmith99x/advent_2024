import argparse
from utils import create_char_map

def count_xmas_pt1(input_file: str) -> int:

    answer = 0

    with open(input_file, "r") as file:
        lines = file.readlines()

    char_map = create_char_map(lines)

    for row_index, column_index in char_map["X"]:
        for delta_row, delta_column in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            for i, char in enumerate("MAS", 1):
                if (row_index + delta_row*i, column_index + delta_column*i) not in char_map[char]:
                    break
            else:
                answer += 1

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count of the word xmas in a 2d grid.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    count_xmas_pt1(args.input_file)