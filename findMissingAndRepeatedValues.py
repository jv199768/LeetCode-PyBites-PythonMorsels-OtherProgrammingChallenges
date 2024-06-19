class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = [0]*(n*n + 1)
        for row in grid:
            for value in row:
                count[value] += 1
        
        answer = [0,0]
        for i in range(0, n*n+1):
            if count[i] == 2:
                answer[0] = i
            elif count[i] == 0:
                answer[1] = i
        return answer
        
