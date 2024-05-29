
# Online Python - IDE, Editor, Compiler, Interpreter
'''In this Bite you will swap case all pybites characters (both lower- and upper case) for a given text.

Not much more as for our instruction, just complete convert_pybites_chars which should work like this:'''

PYBITES = "Today we added TWO NEW Bites to our Platform, exciting!"

def convert_pybites_chars(text: str) -> str:
    result = []
    for word in text.split(" "):
        chars = []
        for char in word:
            if char.islower():
                chars.append(char.upper())
            if char.isupper():
                chars.append(char.lower())
        else:
            chars.append(char)
        result.append(" ".join(chars))
    return " ".join(result)
        
    

print(convert_pybites_chars("Today we added TWO NEW Bites to our Platform, exciting!"))
        
        
