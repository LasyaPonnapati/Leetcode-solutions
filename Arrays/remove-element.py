# LeetCode 27. Remove Element
# Given an integer array nums and an integer val, remove all occurrences of val in-place.
# The order of the elements may be changed. Return the number of elements not equal to val.

# Two-pointer approach: x starts at 0, y starts at n-1.
# x moves forward until nums[x] == val, y moves backward until nums[y] != val, then swap.
# When x >= y, return x.

# Time Complexity: O(n) - x and y each move across the array at most once.
# Space Complexity: O(1) - only two pointer variables are used.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x, y = 0, len(nums) - 1

        while x < y:
            if nums[x] != val:
                x += 1
            if nums[y] == val:
                y -= 1
            if x < y:
                nums[x], nums[y] = nums[y], nums[x]

        # Single element left: count it only if it is not equal to val.
        if x == y and nums[x] != val:
            return x + 1
        return x
