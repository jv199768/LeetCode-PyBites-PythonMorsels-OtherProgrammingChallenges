'''In this Bite you are going to print a chessboard to stdout (use print).

Complete create_chessboard that takes an optional argument size which sets the dimensions of the board (or grid).

This is how it should work:'''


# Online Python - IDE, Editor, Compiler, Interpreter

def chessboard(size):
    finalSentence1 = ""
    finalSentence2 = ""
    v1 = []
    v2 = [] 
    for i in range(size):
        if i%2 == 0: #
            v1.append('#')
            v2.append(' ')
        else:
            v1.append(' ')
            v2.append('#')
    print(v1)
    print(v2)
    
print(chessboard(2))
        

            
