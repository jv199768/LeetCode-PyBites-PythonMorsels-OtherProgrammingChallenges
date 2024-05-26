from bisect import bisect_left
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
            # Get the length of the input list
        n = len(nums)
        # If the list is empty, return 0
        if n == 0:
            return 0
        # Initialize the minimum subarray length to a large value
        ans = float('inf')
        # Create a new list "sums" with size n+1, initialized to all zeros
        sums = [0] * (n + 1)
        # Compute the running sum of nums and store it in "sums"
        for i in range(1, n + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
        # Iterate through each starting index i
        for i in range(1, n + 1):
            # Calculate the target sum for the subarray starting at index i
            to_find = target + sums[i - 1]
            # Find the first element in "sums" that is >= to_find
            bound = bisect_left(sums, to_find)
            # If such an element is found and it is not equal to to_find itself
            if bound != len(sums) and sums[bound] != to_find:
                # Compute the length of the subarray and update ans if necessary
                length = bound - (i - 1)
                ans = min(ans, length)
        # Return ans if it was updated, otherwise return 0
        return ans if ans != float('inf') else 0


        
