# LeetCode 771. Jewels and Stones
# You are given strings jewels representing the types of stones that are
# jewels, and stones representing the stones you have. Each character in
# stones is a type of stone you have. Return how many of the stones you
# have are also jewels. Letters are case sensitive, so "a" is different
# from "A".

# Approach 1 (nested loops):
# 1. Start count at 0.
# 2. For each jewel type i in jewels, scan every stone j in stones.
# 3. If j matches i, add 1 to count.
# 4. Return count.

# Time Complexity: O(j * s) - j is the length of jewels and s is the
# length of stones. For every jewel character we walk the whole stones
# string once.
# Space Complexity: O(1) - only the count variable is stored.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for i in jewels:
            for j in stones:
                if j == i:
                    count += 1
        return count


# Approach 2 (set lookup):
# 1. Put every jewel character into a set so each type is stored once.
# 2. Walk stones once. If a stone is in the set, add 1 to count.
# 3. Return count.
# Checking a set is about O(1) on average, so you no longer rescan
# jewels for every stone.

# Time Complexity: O(j + s) - build the set in O(j), then scan stones
# once in O(s).
# Space Complexity: O(j) - the set stores unique jewel types (at most
# the length of jewels; in practice at most 52 letters).


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0
        for j in stones:
            if j in jewel_set:
                count += 1
        return count


# Approach 3 (fixed-size mark array):
# Letters are ASCII, so there are only 128 possible characters.
# 1. Make a list of 128 False values.
# 2. For each jewel, mark is_jewel[ord(i)] = True.
# 3. Walk stones once. If that character is marked, add 1 to count.
# Same one-pass idea as the set, but lookup is a list index (no hashing).

# Time Complexity: O(j + s) - mark jewels, then scan stones once.
# You still have to read both strings, so this cannot beat O(j + s).
# Space Complexity: O(1) - the list size is always 128, independent of
# j and s.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        is_jewel = [False] * 128
        for i in jewels:
            is_jewel[ord(i)] = True
        count = 0
        for j in stones:
            if is_jewel[ord(j)]:
                count += 1
        return count
