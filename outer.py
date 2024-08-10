
# Online Python - IDE, Editor, Compiler, Interpreter

def outer():
    def inner():
        return "Hello world from inner"
    return inner
    
    
returned_inner_function = outer()
print(returned_inner_function())
