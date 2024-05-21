
# Online Python - IDE, Editor, Compiler, Interpreter
#import operator as op

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 10
#digits = "0123456789"

def filter_names(names):
    t = 0
    result = []
    err = False
    for name in names:
        if name:
        
            if name[0] == IGNORE_CHAR:
                break
            
            for c in [v for v in name]:
                if c in [str(i) for i in range(1, 10)]:
                    break
            
            if name[0] == QUIT_CHAR or t == MAX_NAMES:
                return result
            
            if not err:
                t += 1
                result.append(name)
        
        return result

            
            
        
            
            
                    
            
        
    
    
    
