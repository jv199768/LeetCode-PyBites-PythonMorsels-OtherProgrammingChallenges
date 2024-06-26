
# Online Python - IDE, Editor, Compiler, Interpreter

data = b'\x01\x02'
result = int.from_bytes(data, 'big')
print(result)
result2 = int.from_bytes(data, 'little')
print(result2)
