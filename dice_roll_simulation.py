class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        from typing import List
from functools import lru_cache

class Solution:
    def dieSimulator(self, n: int, roll_max: List[int]) -> int:
        # Adding memoization to avoid repeated calculations
        @lru_cache(None)
        def roll_dice(roll_count, last_roll, consec_roll_count):
            # Base case: all rolls are done
            if roll_count >= n:
                return 1
          
            # Initialize the number of sequences to 0
            num_sequences = 0
          
            # Loop through each possible die face (1 through 6)
            for die_face in range(1, 7):
                # If the current die face is not the same as the previous roll
                if die_face != last_roll:
                    # Roll the die changing the last roll to the current and reset the consecutive roll count to 1
                    num_sequences += roll_dice(roll_count + 1, die_face, 1)
                # If the current die face is the same and consecutive roll count is less than allowed max
                elif consec_roll_count < roll_max[last_roll - 1]:
                    # Roll the die without changing the last roll and increment consecutive roll count
                    num_sequences += roll_dice(roll_count + 1, last_roll, consec_roll_count + 1)
          
            # Return the result modulo 10^9 + 7 to keep the number within integer range for large results
            return num_sequences % (10**9 + 7)

        # Start the recursion with roll_count=0, last_roll=0, and consec_roll_count=0
        return roll_dice(0, 0, 0)
        
