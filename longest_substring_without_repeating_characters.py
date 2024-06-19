class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_seq = 1
        str_len = len(s)
        if str_len == 0:
            return 0
        for i in range(str_len-1):
            j = i+1
            count = 1
            check = set(s[i])
            while j < str_len and (s[j] not in check):
                check.add(s[j])
                count += 1
                j += 1
            if count > max_seq:
                max_seq = count
        return max_seq

        
