class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s
        arr = ['']*numRows
        step = -1
        curr_row = 0
        for char in s:
            arr[curr_row] += char 
            if curr_row == 0 or curr_row == numRows-1:
                step = -step

            curr_row += step

        return ''.join(arr)

        
        
        
