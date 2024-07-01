from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a counter object for all characters in the magazine
        char_count = Counter(magazine)
      
        # Check each character in the ransom note
        for char in ransomNote:
            # Decrement the count for this character in the counter
            char_count[char] -= 1
          
            # If count goes below zero, we cannot construct the note from the magazine
            if char_count[char] < 0:
                return False
      
        # If we haven't returned False, we can construct the ransom note
        return True
        
