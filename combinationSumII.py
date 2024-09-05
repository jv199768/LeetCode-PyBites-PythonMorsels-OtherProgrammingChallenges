class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start_index, path, remaining):
            if remaining == 0:
                ans.append(path[:])
            for i in range(start_index, len(candidates)):
                if remaining - candidates[i] < 0:   # avoid results exceeding target
                    break
                elif i != start_index and candidates[i] == candidates[i-1]: # avoid duplicates
                    continue
                path.append(candidates[i])
                dfs(i+1, path, remaining - candidates[i])
                path.pop()
        candidates.sort()
        ans = []
        dfs(0, [], target)
        return ans
