'''Given an integer number, find the most frequent digit in it.

Examples:

1998 -> two 9's, one 1, one 8 so return 9
177 -> return 7
2020 -> there is 2 two's, 2 zero's. Return 2 = the first highest hitter
12345 -> all digits occur once, so like the last example return the first digit = 1'''
# Python3 program to find the most 
# frequent element in an array. 
def mostFrequent(number):
  arr = [int(x) for x in str(number)]
  n = len(arr)
  maxcount = 0; 
  element_having_max_freq = 0; 
  for i in range(0, n): 
    count = 0
    for j in range(0, n): 
      if(arr[i] == arr[j]): 
        count += 1
    if(count > maxcount): 
      maxcount = count 
      element_having_max_freq = arr[i] 
    
  return element_having_max_freq; 
