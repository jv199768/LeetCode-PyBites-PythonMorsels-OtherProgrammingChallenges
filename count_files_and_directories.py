'''Bite 161. Count the number of files and directories'''
import os
# folder path
dir_path = r'E:\account'
count = 0
count_2 = 0
my_tuple = ()
for path in os.listdir(dir_path):
    count += 1 #count each directory
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        count_2 += 1
new_tuple = my_tuple + (count, count_2)

return new_tuple
