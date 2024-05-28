'''If you worked with Flask or Django you must have seen routes being decorated to enforce authentication.

In this Bite you will write your own login checking decorator.

We simplify the request / session stuff by using 2 hardcoded lists:'''

from functools import wraps
known_users = ['bob', 'julian', 'mike', 'carmen', 'sue']
loggedin_users = ['mike', 'sue']

def login_required(func):
    @wraps(func)
    def inner_func(user):
        msg = " "
        if user not in known_users:
            msg = "please create an account"
        if user in known_users:
            if user not in loggedin_users:
                msg = "please log in"
        return func(f"{msg}")
    return inner_func

@login_required
def welcome(user: str):
    print(user)

        
        
