from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total_elements = n + m
        total_elements_on_left = (total_elements + 1) // 2
        
        low, high = 0, n
        
        while low <= high:
            middle1 = (low + high) // 2
            middle2 = total_elements_on_left - middle1
            
            l1 = nums1[middle1 - 1] if middle1 > 0 else float('-inf')
            r1 = nums1[middle1] if middle1 < n else float('inf')
            
            l2 = nums2[middle2 - 1] if middle2 > 0 else float('-inf')
            r2 = nums2[middle2] if middle2 < m else float('inf')
            
            if l2 > r1:
                low = middle1 + 1
            elif l1 > r2:
                high = middle1 - 1
            else:
                if total_elements % 2 != 0:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2
        
        return 0.0


        
