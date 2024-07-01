class Solution:
    def isPalindrome(self, s: str) -> bool:
            # Initialize pointers
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1
        # Check all letters in the string 
        while left < right:
            # If letters are not equal
            # Decision -> Return False
            if s[left] != s[right]:
                return False  
            # Else, the letters are equal
            # Decision -> Bring left and right closer and compare again
            else:
                left += 1        
                right -= 1
        return True  
        
