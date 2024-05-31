DOT = '.'
TEXTS = ['Hello world', 'Welcome to PyBites',
         'Decorators for fun and profit']
def strip_range(start, end):

        @strip_range(3, 5)
        def gen_output(text):
            return text
    

        def wrap(func):
            def wrapped(text, *args, **kwargs):
                _start = max(start, 0)
                if end > 0:
                    _end = min(len(text), end)
                else:
                    _end =  0
                result = (text[:_start], text[_start:_end], text[_end:])
            return func(f'{result[0]}{DOT * len(result[1])}{result[2]}')

            return wrapped

        return wrap

def test_strip_range(start, end, arg, expected):
    @strip_range(start, end)
    def gen_output(text):
        return text
    actual = gen_output(text=arg)
    assert actual == expected
