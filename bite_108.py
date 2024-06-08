
# Online Python - IDE, Editor, Compiler, Interpreter
from collections import namedtuple

BeltStats = namedtuple('BeltStats', 'score ninjas')

ninja_belts = {'yellow': BeltStats(50, 11),
               'orange': BeltStats(100, 7),
               'green': BeltStats(175, 1),
               'blue': BeltStats(250, 5)}

def get_total_points(belts):
    total_scores = []
    
    for i in belts:
        total_scores.append(int(belts[i].score * belts[i].ninjas))
        
    return sum(total_scores)


print(get_total_points(ninja_belts))
