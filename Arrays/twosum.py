# LeetCode 1. Two Sum
# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# Approach:
# 1. Sort the array (pair each value with its original index first, so we can return correct indexes).
# 2. Use two pointers: x at index 0 and y at last index.
# 3. If both elements add up to target, return their original indexes.
# 4. If sum < target, move x forward; if sum > target, move y backward.
# 5. Continue until sum is found or x index >= y index.

# Time Complexity: O(n log n) - sorting takes O(n log n), and the two-pointer scan is O(n).
# Space Complexity: O(n) - we store value-index pairs before sorting.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = sorted((num, i) for i, num in enumerate(nums))
        x, y = 0, len(indexed_nums) - 1

        while x < y:
            current_sum = indexed_nums[x][0] + indexed_nums[y][0]
            if current_sum == target:
                return [indexed_nums[x][1], indexed_nums[y][1]]
            elif current_sum < target:
                x += 1
            else:
                y -= 1

        return []
