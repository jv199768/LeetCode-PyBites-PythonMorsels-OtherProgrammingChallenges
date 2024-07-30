
# Online Python - IDE, Editor, Compiler, Interpreter

import uuid 

# This will import and generate a unique ideniftier for our unique name


for i in range(int(input('How many EC2 instances would you like unique names for? '))):

# This will prompt the user for the # of EC2 instances in the "range" function

    print(f"{input('What is the name of your department? ')}-{uuid.uuid4()}")
    i += 1

# Each instance will have user for the department name and will print the unique EC2 name based on the format "department-uuid"
