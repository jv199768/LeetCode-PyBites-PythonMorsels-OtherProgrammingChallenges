import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closestSum = sys.maxsize
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if(abs(target-closestSum) > abs(target- (nums[i]+ nums[j] + nums[k]))):
                        closestSum = (nums[i] + nums[j] + nums[k])
                    return closestSum

        
