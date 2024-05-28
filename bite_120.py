
# Online Python - IDE, Editor, Compiler, Interpreter

from functools import wraps

def int_args(func):
    @wraps(func)
    def inner_wrap(*args):
        if not [isinstance for i, int in enumerate(args)]:
            raise TypeError('Something that was not an integer was passed')
        if not all ([i>=0 for i in args]):
            raise ValueError('A negative integer was passed')
        return func(*args)
    return inner_wrap

@int_args
def foo (*args):
    return sum(args)

if __name__ == "__main__":
    print(foo(1, 2, 3, -4, 5))  # error
    print(foo(1, 2, '3', 4, 5))  # error
    print(foo(1, 2, 3, 4, 5))  # ok
            
