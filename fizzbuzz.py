# Online Python - IDE, Editor, Compiler, Interpreter
#Fizz Buzz Algorithm
def fizzBuzz(num):
    result = []
    for i in range(1, num + 1):
        if((i%3) and (i%5)==0):
            result.append("Fizz Buzz")
        elif (i%3 == 0):
            result.append("Fizz")
        elif (i%5 == 0):
            result.append("Buzz")
        else:
            result.append(str(i))
    print(result)
    return result
