
# Online Python - IDE, Editor, Compiler, Interpreter
'''A pangram, according to the Oxford English Dictionary, is a sentence or verse that contains all of the letters of the alphabet.

Given a string containing only English letters, write a function that returns True if sentence is a pangram or False otherwise.

Make sure to remove any whitespace and lowercase the string.'''
import re
import collections
 
def validate_pangram(string):
    # Remove all non-alphabetic characters from the string and convert to lowercase
    string = re.sub('[^a-z]', '', string.lower())
    # Count the occurrence of each alphabet in the string
    counter = collections.Counter(string)
    # Check if the count of unique alphabets is equal to 26
    return len(counter) == 26


 
