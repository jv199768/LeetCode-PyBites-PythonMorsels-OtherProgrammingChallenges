class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        # Get the total number of bombs
        num_bombs = len(bombs)
      
        # Build adjacency list: graph[i] contains bombs that bomb i can detonate
        graph = [[] for _ in range(num_bombs)]
      
        # Check each pair of bombs to see if one can detonate the other
        for i in range(num_bombs - 1):
            x1, y1, radius1 = bombs[i]
            for j in range(i + 1, num_bombs):
                x2, y2, radius2 = bombs[j]
              
                # Calculate Euclidean distance between bombs
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
              
                # If bomb i can reach bomb j with its blast radius
                if distance <= radius1:
                    graph[i].append(j)
              
                # If bomb j can reach bomb i with its blast radius
                if distance <= radius2:
                    graph[j].append(i)
      
        # Try detonating each bomb as the starting point
        max_detonations = 0
      
        for start_bomb in range(num_bombs):
            # Track which bombs have been detonated
            visited = {start_bomb}
          
            # BFS queue to process chain reactions
            queue = [start_bomb]
          
            # Process all bombs that can be detonated in chain reaction
            for current_bomb in queue:
                for neighbor_bomb in graph[current_bomb]:
                    if neighbor_bomb not in visited:
                        visited.add(neighbor_bomb)
                        queue.append(neighbor_bomb)
          
            # Early termination: if all bombs detonated, return immediately
            if len(visited) == num_bombs:
                return num_bombs
          
            # Update maximum number of detonations
            max_detonations = max(max_detonations, len(visited))
      
        return max_detonations
        
