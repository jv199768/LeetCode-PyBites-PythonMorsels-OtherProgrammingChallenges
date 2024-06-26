# Python Code 

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        res = set() # only distinct combinations in the result set

        self.ksum(nums, res, combo=[], k=4, start=0, target=target)
        return [list(tup) for tup in res]


    def ksum(self, nums, res, combo, k, start, target):
        if k == 2:
            # typical two-sum solution
            left, right = start, len(nums) - 1
            while left < right:
                curr_sum = nums[left] + nums[right]
                if  curr_sum == target:
                    res.add(tuple(combo + [nums[left], nums[right]]))
                    left, right = left + 1, right - 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for j in range(start, len(nums) - k + 1):
                self.ksum(
                    nums, res, combo + [nums[j]], k - 1, j + 1, target - nums[j]
                )
