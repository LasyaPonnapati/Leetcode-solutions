# LeetCode 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Approach:
# 1. Sort the array of strings.
# 2. After sorting, the first string (strs[0]) and the last string (strs[-1])
#    are the most different, so their common prefix is also common to every string in between.
# 3. Compare strs[0] and strs[-1] character by character from the start.
# 4. Return the matching prefix.

# Time Complexity: O(n log n * m) - sorting n strings costs O(n log n * m),
# where m is the length of the strings; the prefix scan is O(m).
# Space Complexity: O(1) extra besides sorting - we only walk two strings and
# build the prefix (Python's sort may use extra memory internally).

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[-1]
        prefix = []

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            prefix.append(first[i])

        return "".join(prefix)
