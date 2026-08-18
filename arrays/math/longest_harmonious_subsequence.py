# LeetCode 594. Longest Harmonious Subsequence
# We define a harmonious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious
# subsequence among all its possible subsequences.

# Approach: Brute Force
# 1. Treat each index i as the leftmost number (ele) of a candidate subsequence.
# 2. Scan only to the right of i.
# 3. Build two possible pairs separately: (ele, ele + 1) and (ele, ele - 1).
#    Do not mix both neighbors in the same subsequence.
# 4. A pair is valid only if the neighbor value appears at least once.
# 5. Keep the maximum valid length.

# Time Complexity: O(n^2) - for each of n elements we scan the rest of the array.
# Space Complexity: O(1) - only a few counters are used; no extra list or map.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        max_len = 0

        for i in range(len(nums)):
            ele = nums[i]
            count_plus = 1
            count_minus = 1
            has_plus = False
            has_minus = False

            for j in range(i + 1, len(nums)):
                if nums[j] == ele:
                    count_plus += 1
                    count_minus += 1
                elif nums[j] == ele + 1:
                    count_plus += 1
                    has_plus = True
                elif nums[j] == ele - 1:
                    count_minus += 1
                    has_minus = True

            if has_plus:
                max_len = max(max_len, count_plus)
            if has_minus:
                max_len = max(max_len, count_minus)

        return max_len


#Approach: Hash Map
# 1. Count how many times each number appears in the whole array.
# 2. For every number ele, a valid subsequence can use only (ele and ele + 1) and the neighbor must appear at least once.
# 3. If the neighbor exists, the subsequence length is count(ele) + count(neighbor).
# 4. The answer is the maximum length among all such pairs.

# Time Complexity: O(n) - we count all n elements once, then check each unique number.
# Space Complexity: O(n) - the frequency map stores at most n distinct numbers.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_len = 0
        for ele in freq:
            if ele + 1 in freq:
                max_len = max(max_len, freq[ele] + freq[ele + 1])

        return max_len  