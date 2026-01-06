from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        # Group indices by their corresponding values in nums
        value_to_indices = defaultdict(list)
        for index, value in enumerate(nums):
            value_to_indices[value].append(index)
      
        # Initialize result array with zeros
        result = [0] * len(nums)
      
        # Process each group of indices that have the same value
        for indices in value_to_indices.values():
            # Initialize sum of distances to the left and right of first element
            # left_sum: sum of distances from current position to all indices on the left
            # right_sum: sum of distances from current position to all indices on the right
            left_sum = 0
            right_sum = sum(indices) - len(indices) * indices[0]
          
            # Calculate distance sum for each index in this group
            for i in range(len(indices)):
                # Total distance is sum of left distances and right distances
                result[indices[i]] = left_sum + right_sum
              
                # Update left_sum and right_sum for next iteration
                if i + 1 < len(indices):
                    # Gap between current and next index
                    gap = indices[i + 1] - indices[i]
                    # All (i + 1) indices on the left will contribute this gap
                    left_sum += gap * (i + 1)
                    # All remaining indices on the right will reduce by this gap
                    right_sum -= gap * (len(indices) - i - 1)
      
        return result
        
