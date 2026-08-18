# LeetCode 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.

# Approach:
# 1. The full range [0, n] should contain numbers 0 to n. Here, one number is missing.
# 2. Compute range_sum = sum of 0 to n-1 using sum(range(n)).
# 3. Compute list_sum by adding all numbers in nums.
# 4. The difference list_sum - range_sum gives the missing number.
# 5. If the difference is 0, every number from 0 to n-1 is present, so the missing number is n.

# Time Complexity: O(n) - one pass to compute list_sum; range_sum is computed in O(n).
# Space Complexity: O(1) - only a few variables are used.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        range_sum = sum(range(n))
        list_sum = 0
        for num in nums:
            list_sum += num
        difference = list_sum - range_sum
        if difference == 0:
            return n
        return difference
