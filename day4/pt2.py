import argparse
from utils import create_char_map

def count_xmas_pt2(input_file: str) -> int:

    answer = 0

    with open(input_file, "r") as file:
        lines = file.readlines()

    char_map = create_char_map(lines)

    upleft = lambda row_index, colum_index: (row_index-1, colum_index-1)
    upright = lambda row_index, colum_index: (row_index-1, colum_index+1)
    downleft = lambda row_index, colum_index: (row_index+1, colum_index-1)
    downright = lambda row_index, colum_index: (row_index+1, colum_index+1)

    for r, c in char_map["A"]:
        """
        M S
         A 
        M S 
        """
        if upleft(r, c) in char_map["M"] and downleft(r, c) in char_map["M"]:
            if upright(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
                answer += 1

        """
        M M
         A 
        S S 
        """
        if upleft(r, c) in char_map["M"] and upright(r, c) in char_map["M"]:
            if downleft(r, c) in char_map["S"] and downright(r, c) in char_map["S"]:
                answer += 1 

        """
        S M
         A 
        S M 
        """
        if upright(r, c) in char_map["M"] and downright(r, c) in char_map["M"]:
            if upleft(r, c) in char_map["S"] and downleft(r, c) in char_map["S"]:
                answer += 1 

        """
        S S
         A 
        M M 
        """
        if downleft(r, c) in char_map["M"] and downright(r, c) in char_map["M"]:
            if upleft(r, c) in char_map["S"] and upright(r, c) in char_map["S"]:
                answer += 1 

    print(answer)
    return answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count of the word xmas in a 2d grid.")
    parser.add_argument("input_file", help="The path to the input file.")
    args = parser.parse_args()
    count_xmas_pt2(args.input_file)