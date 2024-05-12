'''It's time to get mathematical! In this Bite we ask that you complete the round_up_or_down function that receives a transactions list of floats and an optional up argument.

If up is True (default) you round them up to the nearest full integer, if it is False, you round down to the nearest full integer. Return a new list with the rounded int values.

Use whatever method you see fit, good luck!'''
# Online Python - IDE, Editor, Compiler, Interpreter
import math

def round_up_or_down(transactions, up):
    new_list = [] 
    if(up):
        new_list = [math.ceil(x) for x in transactions]      
        return new_list
    else:
        new_list = [math.floor(x) for x in transactions]        
        return new_list
   
