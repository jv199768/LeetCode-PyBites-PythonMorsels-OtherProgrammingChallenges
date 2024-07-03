# Runtime: 57 ms, faster than 47.63% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.3 MB, less than 40.19% of Python3 online submissions for Generate Parentheses.

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = ['()']
        if n == 1:
            return res
        n -= 1
        while n:
            tmp = set()
            for r in res:
                for i in range(len(r)+1):
                    tmp.add(r[:i] + '(' + r[i:] + ')')
            res = tmp
            n -= 1
        return(res)
