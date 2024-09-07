
# Online Python - IDE, Editor, Compiler, Interpreter
# Import NumPy library 

import numpy as np 

# Create two multidimensional arrays of 
# integer values 
np_arr1 = np.array([[6, 13, 22, 7, 12], 
					[7, 11, 16, 32, 9]]) 
np_arr2 = np.array([[44, 20, 8, 35, 10], 
					[98, 23, 42, 6, 13]]) 

# Print the array values 
print("\nThe values of the first array :\n", np_arr1) 
print("\nThe values of the second array :\n", np_arr2) 

# Create a new array from two arrays based on 
# the conditions 
new_arr = np.where(((np_arr1 % 2 == 0) & (np_arr2 % 2 == 1)), 
				np_arr1, np_arr2) 

# Print the new array 
print("\nThe filtered values of both arrays :\n", new_arr) 
