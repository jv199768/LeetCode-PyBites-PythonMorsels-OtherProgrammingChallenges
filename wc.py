# Online Python - IDE, Editor, Compiler, Interpreter
'''In this Bite you will convert Unix' wc command into Python. Your function takes a file (absolute path), reads it in and calculates the lines/words/chars. It returns a string of these numbers and the filename, like as a typical wc output, for example:'''
def counter(fname):
    num_spaces = 0
    num_words = 0
    num_lines = 0
    num_charc = 0
    with open (fname,'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if(letter != '' and word == 'Y'):
                    num_words += 1
                    word = 'N'
                elif(letter == ' '):
                    num_spaces +=1
                    word = 'Y'
                
            for i in letter:
                if(i != "" and i!="/n"):
                    num_charc +=1
    print(f"{num_lines}\t{num_words}\t{num_charc}")
