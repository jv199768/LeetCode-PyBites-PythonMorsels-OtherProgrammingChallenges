
# Online Python - IDE, Editor, Compiler, Interpreter
from typing import Any
from typing import Iterable
from typing import Set
from functools import reduce

def intersection(*args: Iterable) -> Set[Any]:
    iterables = [set(iterable) for iterable in args if iterable]
    if iterables:
        return set.intersection(*iterables)

