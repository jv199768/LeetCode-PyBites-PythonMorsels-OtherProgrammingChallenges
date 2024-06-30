class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        """
        :type n: int
        :rtype: List[str]
        """
        res = []

        def dfs(open_count, close_count, sub):
            if open_count + close_count == n * 2:
                res.append(''.join(sub))
                return

            if open_count > close_count:
                sub.append(')')
                dfs(open_count, close_count + 1, sub)
                sub.pop()

            if open_count < n:
                sub.append('(')
                dfs(open_count + 1, close_count, sub)
                sub.pop()

        dfs(0, 0, [])
        return res
        
