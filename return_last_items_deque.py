from collections import deque
import itertools
def my_queue(iterable, n):
    it = iter(iterable)
    d = deque(itertools.islice(it,n))
    return(d)
