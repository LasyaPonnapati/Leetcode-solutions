# LeetCode 485. Max Consecutive Ones
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Approach:
# 1. Scan the array from left to right.
# 2. When nums[i] is 1, increase count by 1 and update max_count if count is larger.
# 3. When nums[i] is 0, reset count to 0 because the consecutive streak breaks.
# 4. Return max_count after checking all elements.

# Time Complexity: O(n) - we visit each element once in a single pass.
# Space Complexity: O(1) - only count and max_count variables are used.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        max_count=0
        for i in range(0,n):
            if nums[i]==1:
                count+=1
                if count > max_count:
                    max_count=count
            else:
                count=0
        return max_count
