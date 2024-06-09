
# Online Python - IDE, Editor, Compiler, Interpreter

from collections import namedtuple
import datetime
import json
from typing import NamedTuple

blog = dict(name='PyBites',
            founders=('Julian', 'Bob'),
            started=datetime.datetime(year=2016, month=12, day=19),
            tags=['Python', 'Code Challenges', 'Learn by Doing'],
            location='Spain/Australia',
            site='https://pybit.es')

# define namedtuple here
Blog = namedtuple('Blog', blog.keys())


def dict2nt(dict_):
    return Blog(**dict_)

# Define a custom function to serialize datetime objects 
def serialize_datetime(obj): 
    if isinstance(obj, datetime.datetime): 
        return obj.isoformat() 

def nt2json(nt):
    start = nt._asdict()
    end = json.dumps(start, default=serialize_datetime)
    return end
