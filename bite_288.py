'''Write a function that accepts a list of digits and returns the smallest number that can be created by combining unique digits.

Therefore, you have to ignore duplicated digits.''' 
# Online Python - IDE, Editor, Compiler, Interpreter
from typing import List

def smallest_number(digits: List[int]) -> int:
    removed_duplicates = set(digits)
    sorted_duplicates = sorted(removed_duplicates)
    if len(sorted_duplicates) == 0:
        return 0
    s = [str(i) for i in sorted_duplicates]
    res = int("".join(s))
    return res


 
        
