
# Online Python - IDE, Editor, Compiler, Interpreter
"""[Summary]
:param [numbers]: [A list of integers, defaults to None]
:type [numbers]: [int or None]
...
:return: [total sum of numbers if numbers if is not None, otherwise the total sum of the numbers between 1 and 100]
:rtype: [integer]
"""

def sum_numbers(numbers=None):
    if numbers != None:
        total = 0
        for number in numbers:
            total += number
        return total
    else:
        return sum([x for x in range(1, 100)])

    
    
    
