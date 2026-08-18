# LeetCode 704. Binary Search
# Given a sorted array of integers nums (ascending) and an integer target,
# search for target. If it exists, return its index. Otherwise return -1.
# You must write an algorithm with O(log n) runtime complexity.

# Approach:
# 1. Keep a search window with left (l) at the start and right (r) at the end.
# 2. While the window is valid (l <= r), look at the middle index m.
# 3. If nums[m] is the target, return m.
# 4. If nums[m] is greater than target, the target (if present) is on the left, so move r to m - 1.
# 5. If nums[m] is less than target, the target (if present) is on the right, so move l to m + 1.
# 6. If the window becomes empty, target is not in the array.

# Time Complexity: O(log n) - each step cuts the search window in half.
# Space Complexity: O(1) - only left, right, and mid indexes are stored.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
