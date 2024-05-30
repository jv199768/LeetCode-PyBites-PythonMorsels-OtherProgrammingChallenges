
# Online Python - IDE, Editor, Compiler, Interpreter

from functools import singledispatch

@singledispatch
def count_down(arg):
    raise ValueError


@count_down.register(str)
def _(arg):
    while arg:
        print(arg)
        arg = arg[:-1]
        
@count_down.register(int)
@count_down.register(float)
def _(arg):
    count_down(str(arg))

@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(data_type):
    str_data = ''.join([str(x) for x in data_type])
    count_down(str_data)

@count_down.register(dict)
def _(arg):
    count_down(list(arg.keys()))
