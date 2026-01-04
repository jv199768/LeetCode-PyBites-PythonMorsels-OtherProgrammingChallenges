class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
      
        // Queue to store positions of rotten oranges for BFS
        Deque<int[]> queue = new ArrayDeque<>();
      
        // Count of fresh oranges
        int freshCount = 0;
      
        // Initial scan: find all rotten oranges and count fresh ones
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (grid[row][col] == 1) {
                    // Fresh orange found
                    freshCount++;
                } else if (grid[row][col] == 2) {
                    // Rotten orange found, add to queue
                    queue.offer(new int[] {row, col});
                }
            }
        }
      
        // Direction vectors for 4-directional movement (up, right, down, left)
        final int[] directions = {-1, 0, 1, 0, -1};
      
        // BFS to rot adjacent fresh oranges level by level
        for (int minutes = 1; !queue.isEmpty() && freshCount > 0; minutes++) {
            // Process all oranges at current level
            int levelSize = queue.size();
          
            for (int i = 0; i < levelSize; i++) {
                int[] currentPosition = queue.poll();
                int currentRow = currentPosition[0];
                int currentCol = currentPosition[1];
              
                // Check all 4 adjacent cells
                for (int dir = 0; dir < 4; dir++) {
                    int newRow = currentRow + directions[dir];
                    int newCol = currentCol + directions[dir + 1];
                  
                    // Check if the new position is valid and contains a fresh orange
                    if (newRow >= 0 && newRow < rows && 
                        newCol >= 0 && newCol < cols && 
                        grid[newRow][newCol] == 1) {
                      
                        // Rot the fresh orange
                        grid[newRow][newCol] = 2;
                        queue.offer(new int[] {newRow, newCol});
                        freshCount--;
                      
                        // If all fresh oranges are rotten, return the time taken
                        if (freshCount == 0) {
                            return minutes;
                        }
                    }
                }
            }
        }
      
        // Return -1 if fresh oranges remain, 0 if no fresh oranges existed initially
        return freshCount > 0 ? -1 : 0;
    }
}
