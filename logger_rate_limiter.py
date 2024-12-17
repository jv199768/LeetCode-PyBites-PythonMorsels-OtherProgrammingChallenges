
# Online Python - IDE, Editor, Compiler, Interpreter

class Logger:
    def __init__(self):
        self.timestamp = {}
        
    def shouldPrintMessage(self, timestamp:int, message:str) -> bool:
        if message in self.timestamp:
            if timestamp-self.timestamp[message] < 10:
                return False
        self.timestamp[message] = timestamp
        return True
