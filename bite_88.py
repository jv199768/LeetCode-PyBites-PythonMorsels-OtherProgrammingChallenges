'''Bite 88. Write a performance monitoring context manager
It's time for Context Managers part II. In Bite 20 you used it to roll back a transaction implementing the __enter__ and __exit__ dunder methods.'''

from contextlib import contextmanager
from time import time
import sys

OPERATION_THRESHOLD_IN_SECONDS = 2.2
ALERT_THRESHOLD = 3
ALERT_MSG = 'ALERT: There is a performance hit today'

@contextmanager
def timeit():
    violations = 0
    start = time()
    yield
    end = time()
    if end-start >= OPERATION_THRESHOLD_IN_SECONDS:
        dt = datetime.today()
        violations += 1
        if violations >= ALERT_THRESHOLD:
            print(ALERT_MSG)

