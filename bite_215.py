
# Online Python - IDE, Editor, Compiler, Interpreter
'''Complete the validate_license function writing a regular expression that matches a PyBites license key which:

Starts with PB,
following 4 times dash (-) and 8 chars which can be upper case chars or digits,
for example: PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4 would be a valid license key.'''

import re

def validate_license(key: str):
    pattern = r"([PB]{2}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8}-[A-Z0-9]{8})"
    check: re.Pattern = re.compile(pattern)
    
    if check.match(key) and len(key) == 38:
        return True
    else:
        return False
