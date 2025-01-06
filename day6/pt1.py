import argparse
from utils import Lab, Guard

def count_guard_moves_pt1(input_file: str) -> int:

    with open(input_file, "r") as file:
        lines = file.readlines()

    lab = Lab(lines)

    if lab.guard_initial_position != tuple():
        guard = Guard(lab)

    while guard.touring:
        guard.move(lab)

    print(len(guard.positions)) 
    return len(guard.positions)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count of the word xmas in a 2d grid.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    count_guard_moves_pt1(args.input_file)