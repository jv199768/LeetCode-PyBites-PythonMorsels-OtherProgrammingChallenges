# Online Python - IDE, Editor, Compiler, Interpreter
import datetime
def weekday_of_birth_date(year, month, date):
    d = datetime.datetime(year, month, date)
    return d.strftime('%a')
