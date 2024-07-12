    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Case 1: If the middle element is the target
        if nums[mid] == target:
            return mid

        # Case 2: Left half is sorted
        if nums[mid] >= nums[left]:
            # If the target is in the sorted left half
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Case 3: Right half is sorted
        else:
            # If the target is in the sorted right half
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    # Target not found
    return -1
