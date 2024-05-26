# Online Python - IDE, Editor, Compiler, Interpreter
'''Write a simple generator that counts from 100 to 1. It can just return the ints one by one, no fancy forma
tting, just focus on the basic mechanics of generators. Remember that going beyond 1 it would trigger a StopIteration exception.'''


def countdown(default=100):
    while True:
        yield default
        default -= 1
        print(default)
