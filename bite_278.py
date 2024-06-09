# Online Python - IDE, Editor, Compiler, Interpreter

from collections import Counter

def major_n_minor(numbers):
    my_tuple = ()
    majority = Counter(numbers).most_common()
    my_tuple = my_tuple + (majority[0][0], majority[-1][0])   
    return my_tuple
