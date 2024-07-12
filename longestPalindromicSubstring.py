class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        palindrome = ""
        for i in range(len(s)):
            p = 0

            while i-p >=0 and i+p < len(s) and s[i-p] == s[i+p]:
                if 2*p+1 > len(palindrome):
                    palindrome = s[i-p:i+p+1]
                p+=1

            left = i
            right = i+1

            while right < len(s) and left >= 0 and s[left] == s[right]:
                if right - left +1 > len(palindrome):
                    palindrome = s[left:right+1]
                left -=1
                right +=1
    
        return palindrome

        


        

        
