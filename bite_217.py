'''In this Bite you will use it to get the length of a help text as returned by help.'''

# Online Python - IDE, Editor, Compiler, Interpreter
from contextlib import redirect_stdout
from io import StringIO
from types import BuiltinFunctionType

def get_len_help_text (builtin: BuiltinFunctionType) -> int:
    if not isinstance(builtin, BuiltinFunctionType):
        raise ValueError('not a builtinFunctionType')
    
    with redirect_stdout(StringIO()) as f:
        help(builtin)
    s = f.getvalue()
    res = len(s)
    print(res)

print(get_len_help_text(pow))
print(get_len_help_text(max))
print(get_len_help_text('Bogus'))
