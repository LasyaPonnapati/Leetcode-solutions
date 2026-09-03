# LeetCode 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s,
# and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters
# of a different word or phrase, using all the original letters
# exactly once.

# Approach (count characters in a hashmap):
# 1. If s and t have different lengths, they cannot be anagrams.
# 2. Count how many times each character appears in s.
# 3. For each character in t, subtract one from that count.
#    If t has a character that never appeared in s, return False.
# 4. If every count is back to 0, s and t use the same letters
#    the same number of times.

# Time Complexity: O(n) - n is the length of s (and t). We scan
# s once, t once, then the unique keys in the map (at most n).
# Space Complexity: O(1) if the alphabet is fixed (26 lowercase
# letters), otherwise O(k) where k is the number of unique
# characters stored in the map.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = {}
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        for i in t:
            if i not in ans:
                return False
            else:
                ans[i] -= 1
        for val in ans.values():
            if val != 0:
                return False
        return True


# Approach (fixed array of 26 letter counts):
# LeetCode 242 only uses lowercase English letters, so a hashmap is
# more than we need. An array of size 26 is enough.
# 1. If s and t have different lengths, they cannot be anagrams.
# 2. For each index, add 1 for s[i] and subtract 1 for t[i].
# 3. If every slot is 0 at the end, both strings used each letter
#    the same number of times.

# Time Complexity: O(n) - one pass over the strings, then a scan of
# 26 slots (constant).
# Space Complexity: O(1) - the count array is always length 26,
# independent of n.


class SolutionCountArray:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        for val in count:
            if val != 0:
                return False
        return True
