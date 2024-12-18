import argparse
from utils import multiplications_enabled

def uncorrupted_mul_enabled(input_file: str) -> int:
    with open(input_file, "r") as file:
        content = file.read().replace('\n', '')

    answer = multiplications_enabled(content)

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sum of all the uncorupted multiplication results.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    uncorrupted_mul_enabled(args.input_file)