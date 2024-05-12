'''Bite 91. Matching multiple strings'''
# Online Python - IDE, Editor, Compiler, Interpreter

def contains_only_vowels(your_string):
    your_string = your_string.lower()
    vowels = set("aeiou")
    s = set({})
    for char in your_string: 
        if char in vowels:
            s.add(char)
        else: 
            pass
    if len(s) == len(vowels):
        return True
    else: 
        return False
        
def contains_digits(your_string):
    res = your_string.lower().isdigit()
    return res

def contains_any_py_chars(your_string, chars):
    s = set({})
    your_string = your_string.lower()
    your_set = set(chars)
    for char in your_string:
        if char in your_set:
            s.add(char)
        else:
            pass
    
    if len(s) == len(your_set):
        return True
    else:
        return False
