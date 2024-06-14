# Online Python - IDE, Editor, Compiler, Interpreter
from typing import List, TypeVar

T = TypeVar("T", int, float)

def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError

    return [
        int(str(digit * (10 ** (n)))[: n if digit > 0 else n + 1]) for digit in numbers
    ]
