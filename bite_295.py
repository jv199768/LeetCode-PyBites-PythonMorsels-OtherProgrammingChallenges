
# Online Python - IDE, Editor, Compiler, Interpreter
from functools import reduce
'''def chainwithseperator(lis,sep):
  it=iter(lis)
  for item in it.next():
    yield item
  for sublis in it:
    yield sep
    for item in sublis:
      yield item'''

def join_lists(list, separator):
    y=reduce(lambda a,b:a+[separator]+b,list)
    return y


     
print(join_lists([ ['a', 'b'], ['c'] ], '&'))
