'''In this Bite you'll learn to catch and raise Python exceptions.

Write a simple division function meeting the following requirements:

1. When the denominator is zero, catch the corresponding exception and return zero.

2. When the numerator or denominator have an invalid type reraise the corresponding exception.

3. If the result of the division is negative raise a ValueError.'''

# Online Python - IDE, Editor, Compiler, Interpreter

def positive_divide(numerator, denominator):
    if denominator == 0:
        return 0
    try:
        result = numerator / denominator
        if result < 0:
            raise ValueError()
    except TypeError as e:
        raise e
    return result
