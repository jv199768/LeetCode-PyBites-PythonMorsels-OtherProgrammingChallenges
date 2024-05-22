class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum_element = nums[0]

        for i in range(len(nums)):
            if nums[i] < minimum_element:
                minimum_element = nums[i]
        return minimum_element

        

        
        
