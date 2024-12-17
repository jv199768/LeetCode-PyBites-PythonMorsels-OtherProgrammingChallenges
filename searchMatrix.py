class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        row = len(matrix)       
        col = len(matrix[0])    # Number of Columns of the matrix...
        beg = 0
        end = row*col #treating this as a 1D matrix
        while beg < end:
            mid = beg + (end - beg) // 2
            idx = matrix[mid // col][mid % col];
            if idx == target:
                return True
            if idx < target:
                beg = mid + 1
            else:
                end = mid
        return False
        
