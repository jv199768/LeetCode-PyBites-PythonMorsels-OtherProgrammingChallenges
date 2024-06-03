
# Online Python - IDE, Editor, Compiler, Interpreter

import pandas as pd
from string import ascii_lowercase, ascii_uppercase

def basic_series():
    return pd.Series(data = [1,2,3,4,5], name = 'Fred')

def float_series():
    start = 0.000
    end = 1.000
    step = 0.001
    arr = []
    while start <= end:
        start = start + step
        arr.append(start)
        start = round(start, 3)
    return pd.Series(data=arr)

def alpha_index_series():
    return pd.Series(data=list(range(1,27)), index = list(ascii_lowercase))

def object_values_series():
    return pd.Series(data=list(ascii_uppercase), index = list(range(101,127)))
