class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low = 0
        high = len(nums)-1
        res = [-1,-1]

        # Find first Index
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                res[0] = mid
            if nums[mid]<target:
                low = mid + 1
            else:
                high = mid -1

        # Reset end to last idex
        high = len(nums)-1

        # Find Last Index
        while low<=high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                res[1] = mid
            if nums[mid]>target:
                high = mid -1
            else:
                low = mid + 1

        return res
         
