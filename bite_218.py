
# Online Python - IDE, Editor, Compiler, Interpreter
from functools import wraps

UPPER_SLICE = " === Upper bread slice === "
LOWER_SLICE = "=== Lower bread slice === "

def sandwich(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(UPPER_SLICE)
        func(*args, **kwargs)
        print(LOWER_SLICE)
    return wrapper

@sandwich
def add_ingredients(ingredients):
    """add_ingredients

    Paramiters
    ----------
    ingredients:
        List[str]
    """
    print("/ ".join(ingredients))


ingredients = ['bacon', 'lettuce', 'tomato']
print(add_ingredients(ingredients))
