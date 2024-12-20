from collections import defaultdict
from typing import List, Dict, Set

def get_rules(lines: List[str]) -> Dict[str, Set[str]]:
    """
    Parses the input lines to create a mapping of page numbers to their rules.
    """
    page_num_map = defaultdict(set)

    for line in lines:
        if "|" in line:
            before, after = line.split("|")
            after = after.strip()
            page_num_map[before].add(after)
    
    return page_num_map

def correct_order(rules: Dict[str, Set[str]], page_list: List[str]) -> bool:
    """
    Checks if the given page list is in the correct order according to the rules.
    """
    for i, page_num in enumerate(page_list):
        stripped_page_num = page_num.strip()
        for num in page_list[:i]:
            if num in rules[stripped_page_num]:
                return False
    
    return True

def sort_pages(rules: Dict[str, Set[str]], page_list: List[str]) -> List[str]:
    """
    Sorts the page list according to the rules.
    """
    for i, page_num in enumerate(page_list):
        stripped_page_num = page_num.strip()
        for j, num in enumerate(page_list[:i]):
            if num in rules[stripped_page_num]:
                page = page_list.pop(i)
                page_list.insert(j, page)
                return sort_pages(rules, page_list)

    return page_list

def median_page_num(page_list: List[str]) -> int:
    """
    Returns the median page number from the given list.
    """
    middle_index = len(page_list) // 2

    return int(page_list[middle_index].strip())
