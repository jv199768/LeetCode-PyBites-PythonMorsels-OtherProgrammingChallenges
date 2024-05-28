'''Write a decorator called make_html that wraps text inside one or more html tags.

As shown in the tests decorating get_text with make_html twice should wrap the text in the corresponding html tags, so:'''
# Online Python - IDE, Editor, Compiler, Interpreter
from functools import wraps

def make_html(tag: str):
    def tag_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            text = func(*args, **kwargs)
            return f"<{tag}>{text}</{tag}>"
        return wrapper
    return tag_wrapper

@make_html("p")
@make_html("strong")
def get_text(text: str = "Write a decorator with argument"):
    return text

print(get_text())
