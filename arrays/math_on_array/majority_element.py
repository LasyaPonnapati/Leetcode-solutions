# LeetCode 169. Majority Element
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than floor(n / 2) times.
# You may assume that the majority element always exists in the array.

# Approach (Boyer-Moore voting):
# 1. Start with the first number as the current candidate (ele) and give it 1 vote.
# 2. Walk through the rest of the array.
# 3. If the current number matches ele, add 1 vote; otherwise subtract 1 vote.
# 4. If votes drop to 0, the previous candidate is cancelled, so pick the current
#    number as the new candidate and reset votes to 1.
# 5. Because a majority element is guaranteed, the candidate left at the end is
#    the majority element.

# Time Complexity: O(n) - each element is visited once.
# Space Complexity: O(1) - only the candidate and vote count are stored.

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        votes = 1
        for i in range(1, len(nums)):
            if nums[i] == ele:
                votes += 1
            else:
                votes -= 1
            if votes == 0:
                ele = nums[i]
                votes = 1
        return ele
