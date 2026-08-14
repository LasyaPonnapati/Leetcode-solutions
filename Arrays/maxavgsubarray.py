# LeetCode 643. Maximum Average Subarray I
# Given an integer array nums and an integer k, find a contiguous subarray of length k
# that has the maximum average value and return this value.

# Fixed sliding window approach:
# 1. Use x and y as the left and right indices of a window of size k (y = x + k - 1).
# 2. Compute the average of the first window and store it as max_avg.
# 3. Slide the window one step to the right: remove nums[x], add nums[y + 1],
#    and update the average without recomputing the full sum:
#    new_avg = (old_avg * k - nums[x] + nums[y + 1]) / k
# 4. Track the maximum average seen across all windows.

# Time Complexity: O(n) - each element is added to and removed from the window at most once.
# Space Complexity: O(1) - only a few variables are used.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = 0
        y = k - 1
        avg = sum(nums[x:y + 1]) / k
        max_avg = avg
        while y < len(nums) - 1:
            avg = (avg * k - nums[x] + nums[y + 1]) / k
            x += 1
            y += 1
            max_avg = max(max_avg, avg)
        return max_avg
