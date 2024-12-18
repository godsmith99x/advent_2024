from collections import defaultdict


def create_char_map(lines: list[str]) -> dict[str, set[tuple[int, int]]]:
    char_map = defaultdict(set)
    for row_index, row in enumerate(lines):
        for column_index, char in enumerate(row):
            char_map[char].add((row_index, column_index))
    
    return char_map