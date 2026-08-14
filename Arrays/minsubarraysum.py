# LeetCode 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# Variable sliding window approach:
# 1. Use x as the left index and y as the right index (exclusive end of the window).
# 2. Expand the window by adding nums[y] and moving y right while the sum is less than target.
# 3. When the sum is at least target, record the window length (y - x), then shrink from the left.
# 4. Keep expanding and shrinking until y reaches the end and the sum drops below target.
# 5. If no valid window was found, return 0.

# Time Complexity: O(n) - x and y each move across the array at most once.
# Space Complexity: O(1) - only a few variables are used.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        x = 0
        y = 0
        min_len = len(nums) + 1
        window_sum = 0

        while y < len(nums) or window_sum >= target:
            if window_sum >= target:
                min_len = min(y - x, min_len)
                window_sum -= nums[x]
                x += 1
            elif y < len(nums):
                window_sum += nums[y]
                y += 1
            else:
                break

        return 0 if min_len == len(nums) + 1 else min_len
