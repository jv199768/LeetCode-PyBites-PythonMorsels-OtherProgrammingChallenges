'''Explanation:
1. Initialize left_sum and max_sum:
Calculate the sum of the first k elements and store it in left_sum. This represents the initial maximum sum.
2. Iterate from the right:
Iterate from the right side of the array, gradually adding elements to right_sum while subtracting elements from left_sum.
3. Update max_sum:
At each iteration, compare the current left_sum + right_sum with the current max_sum and update max_sum if necessary.
4. Return max_sum:
After the loop, max_sum will contain the maximum points that can be obtained from the cards.'''

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_sum = sum(cardPoints[:k])
        max_sum = left_sum
        right_sum = 0

        for i in range(k - 1, -1, -1):
            left_sum -= cardPoints[i]
            right_sum += cardPoints[len(cardPoints) - k + i]
            max_sum = max(max_sum, left_sum + right_sum)

        return max_sum
        
