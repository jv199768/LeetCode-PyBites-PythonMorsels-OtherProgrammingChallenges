# Python Program to find area of the largest region of 1s

# A function to check if cell(r, c) can be included in DFS
def is_safe(M, r, c, rows, cols):
 
    # row number is in range, column number is in range and
    # value is 1
    return (r >= 0 and r < rows) and (c >= 0 and c < cols) \
  and (M[r][c] == 1)

# Depth-First-Search to visit all cells in the current island
def dfs(M, r, c, rows, cols, area):
   
    # Depth-First-Search to visit all cells in the current island
    # These arrays are used to get row and column
    # numbers of 8 neighbours of a given cell
    dirR = [-1, -1, -1, 0, 0, 1, 1, 1]
    dirC = [-1, 0, 1, -1, 1, -1, 0, 1]
   
    # Increment area of region by 1
    area[0] += 1
   
    # Mark this cell as visited
    M[r][c] = 0

    # Recur for all connected neighbours
    for i in range(8):
        new_r = r + dirR[i]
        new_c = c + dirC[i]
       
        if is_safe(M, new_r, new_c, rows, cols):
            dfs(M, new_r, new_c, rows, cols, area)

# function to find area of the largest region of 1s
def largest_region(M):
 
    # function to find area of the largest region of 1s
    rows = len(M)
    cols = len(M[0])
   
    # Initialize result as 0 and traverse through the
    # all cells of given matrix
    max_area = 0
    for i in range(rows):
        for j in range(cols):
            # If a cell with value 1 is found
            if M[i][j] == 1:
             
              # area is taken as a list of size 1 to
                # achieve pass by reference
                area = [0]
                dfs(M, i, j, rows, cols, area)
               
                # maximize the area
                max_area = max(max_area, area[0])
   
    return max_area

if __name__ == "__main__":
    M1 = [
        [1, 0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0],
        [1, 0, 0, 1, 0, 1, 1]
    ]
   
    M2 = [
        [1, 1, 1 ,1 ,0],
        [1,1,0, 1, 0],
        [1, 1 , 0 , 0 , 0],
        [0 ,0 , 0, 0, 0]
    ]
   
    M3 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    M4 = [[0,0,0,0,0,0,0,0]]

    print(largest_region(M1))
    print(largest_region(M2))
    print(largest_region(M3))
    print(largest_region(M4))
