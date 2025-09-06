class Solution(object):
    def minPatches(self, nums, n):
        patches = 0  # Count of numbers added
        miss = 1     # The smallest number we cannot form
        i = 0        # Index in nums

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # If the current number in nums can extend our reachable range
                miss += nums[i]
                i += 1
            else:
                # If nums[i] is too large or we've exhausted nums,
                # we need to add a patch. The most efficient patch is 'miss' itself,
                # as it extends the reachable range by the largest possible amount
                # while covering the smallest missing number.
                miss += miss
                patches += 1
        return patches
