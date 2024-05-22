'''You are to flesh out the log_it() function so that it will log to any LOG LEVEL and with any message passed to it. You will need to create globalvariables for each of the log levels, since those will be imported into the tests for testing.

LOG LEVELS:'''
# Online Python - IDE, Editor, Compiler, Interpreter
import logging

logger = logging.getLogger('pybites_logger')

DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL

def log_it(callable: logger, msg: str) -> None:
    print(msg)
    print(callable)
    return callable

if __name__ == "__main__":
    log_it(DEBUG, "This is a debug message.")
    log_it(WARNING, "This is a warning message.")
    log_it(INFO, "This is an info message.")
    log_it(ERROR, "This is an error message.")
    log_it(CRITICAL, "This is a critical message.")
