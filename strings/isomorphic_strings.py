# LeetCode 205. Isomorphic Strings
# Given two strings s and t, determine if they are isomorphic.
# Two strings s and t are isomorphic if the characters in s can be
# replaced to get t.
# All occurrences of a character must be replaced with another
# character while preserving the order of characters. No two
# characters may map to the same character, but a character may
# map to itself.

# Approach (one hashmap, check existing values):
# 1. If s and t have different lengths, they cannot be isomorphic.
# 2. Walk s and t together with pointers i and j.
# 3. Store s[i] -> t[j] in a map. If s[i] was already mapped to a
#    different character, return False.
# 4. When adding a new s[i], if t[j] is already a value in the map,
#    some other letter in s already maps to t[j], so return False.

# Time Complexity: O(n) for a fixed alphabet (each values() scan is
# at most 256). In general O(n * k), k = unique keys in the map.
# Space Complexity: O(1) if the alphabet is fixed (at most 256
# ASCII mappings), otherwise O(k) unique characters in the map.


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = {}
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] not in ans:
                if t[j] in ans.values():
                    return False
                ans[s[i]] = t[j]
            else:
                if ans[s[i]] != t[j]:
                    return False
            i += 1
            j += 1
        return True


# Approach (two hashmaps, s -> t and t -> s):
# Same walk as above. A second map stores t[j] -> s[i] so two
# different letters in s cannot map to the same letter in t.
# Each lookup is O(1), so we do not scan ans.values().

# Time Complexity: O(n) - one pass, each dict lookup is O(1).
# Space Complexity: O(1) if the alphabet is fixed (at most 256
# ASCII mappings), otherwise O(k) unique characters in the maps.


class SolutionReverse:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ans = {}
        reverse = {}
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] not in ans:
                ans[s[i]] = t[j]
            else:
                if ans[s[i]] != t[j]:
                    return False
            if t[j] not in reverse:
                reverse[t[j]] = s[i]
            else:
                if reverse[t[j]] != s[i]:
                    return False
            i += 1
            j += 1
        return True
