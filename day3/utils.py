import re

def multiplications(line: str) -> int:
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)

    return sum(int(x) * int(y) for x, y in matches)

def multiplications_enabled(line: str) -> int:
    pattern1 = r"don't\(\).*?do\(\)"
    result1 = re.sub(pattern1, '', line)

    pattern2 = r"don't\(\).*"
    result2 = re.sub(pattern2, '', result1)

    return multiplications(result2)