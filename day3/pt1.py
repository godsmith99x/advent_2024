import argparse
from utils import multiplications

def uncorrupted_mul(input_file: str) -> int:
    with open(input_file, "r") as file:
        content = file.read().replace('\n', '')

    answer = multiplications(content)

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum of all the uncorrupted multiplication results.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    uncorrupted_mul(args.input_file)