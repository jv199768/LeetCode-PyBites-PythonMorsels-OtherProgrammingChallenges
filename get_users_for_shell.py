# Online Python - IDE, Editor, Compiler, Interpreter
'''The /etc/passwd file is a text-based database of information about users that may log into the system or other operating system user identities that own running processes. (Wikipedia).

In this Bite you complete the function get_users_for_shell that takes a /etc/passwd multiline string and a shell to filter on (default bash). Parse the output returning a list of usernames that match the shell.'''

def get_users_for_shell(etc_string):
    new_string = etc_string.splitlines()
    print("\n".join([u.split(":")[0] for u in new_string]))
