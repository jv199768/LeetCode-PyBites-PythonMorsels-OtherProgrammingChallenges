'''Python 3.9 brought an exciting enhancement to the dict built-in class!

Dictionaries can now be merged with the | operator (PEP 584).

This small change lets us write more compact expressions with dictionaries that are easier to read.

Here's an exercise to let you try | out on dictionaries.'''
def combine_and_count(dict1, dict2):
    result_dict = {}
    for key in dict1.keys() & dict2.keys():
        result_dict[key] = dict1[key] | dict2[key]
    for key in dict1.keys() - dict2.keys():
        result_dict[key] = dict1[key]
    for key in dict2.keys() - dict1.keys():
        result_dict[key] = dict2[key]
    return result_dict
