'''Your task is to complete the convert() function. It's purpose is to convert centimeters to inches and vice versa. As simple as that sounds, there are some caveats:

convert():
The function will take value and fmt parameters:
value: must be an int or a float otherwise raise a TypeError
fmt: string containing either "cm" or "in" anything else raises a ValueError.'''
# Online Python - IDE, Editor, Compiler, Interpreter
import math
def convert(value, fmt):
    try: 
        if (fmt == "cm"):
            if isinstance(value, int):
                return round((value / 2.54), 4)
            if isinstance(value, float):
                return round((value / 2.54), 4)
        if(fmt == "in"):
            if isinstance(value, int):
                return round((value * 2.54), 4)
            if isinstance(value, float):
                return round((value * 2.54), 4)
    except TypeError:
        print("You must choose an integer or a float")
    except ValueError: 
        print("Must choose cm or in")

print(convert(5, "cm"))
print(convert(5.21, "cm"))
print(convert(1.96, "in"))
print(convert(2, "in"))
print(convert("Not an integer", "Float"))
            
