# LeetCode 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray
# is called nice if there are k odd numbers on it.
# Return the number of nice subarrays.

# Approach (two pointers x and y):
# 1. Exactly k odds = (at most k odds) - (at most k - 1 odds).
# 2. Expand y. If nums[y] is odd, add 1 to odd_count.
# 3. While the window has more odds than the limit, shrink from x.
# 4. Every subarray ending at y and starting anywhere from x to y is valid
#    for "at most limit", so add (y - x + 1) to count.
# 5. Run that once with limit k, then subtract the same pass with limit k - 1.

# Time Complexity: O(n) - x and y each move across the array at most once.
# Space Complexity: O(1) - only a few pointers and counters are stored.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        x = 0
        y = 0
        count = 0
        odd_count = 0
        while y <= len(nums) - 1:
            if nums[y] % 2 != 0:
                odd_count += 1
            while odd_count > k:
                if nums[x] % 2 != 0:
                    odd_count -= 1
                x += 1
            count += y - x + 1
            y += 1

        x = 0
        y = 0
        odd_count = 0
        while y <= len(nums) - 1:
            if nums[y] % 2 != 0:
                odd_count += 1
            while odd_count > k - 1:
                if nums[x] % 2 != 0:
                    odd_count -= 1
                x += 1
            count -= y - x + 1
            y += 1

        return count

