'''Write a simple generator that counts from 100 to 1. It can just return the ints one by one, no fancy form
atting, just focus on the basic mechanics of generators. Remember that going beyond 1 it would trigger a StopIteration exception.'''

# Online Python - IDE, Editor, Compiler, Interpreter

def countdown(default=100):
    try:
        while default > 1:
            default -= 1
            print(default)
    except StopIteration:
        print("The countdown is now over")
