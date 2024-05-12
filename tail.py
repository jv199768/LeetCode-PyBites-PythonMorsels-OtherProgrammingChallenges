'''Bite 100. Display the last part of a file (Unix tail)'''
def tail (f_name, num_lines):
    with open (f_name, 'r') as f:
        returned_list = []
        lines = f.readlines()
        last_lines = lines[-num_lines:]
        for line in last_lines:
            line = line.rstrip()       
        return last_lines
