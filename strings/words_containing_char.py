# LeetCode 2942. Find Words Containing Character
# You are given a 0-indexed array of strings words and a character x.
# Return an array of indices representing the words that contain the
# character x. The returned array can be in any order.

# Approach:
# 1. Make an empty list ans to store matching indices.
# 2. Walk each word by index i from 0 to len(words) - 1.
# 3. If the character x appears in words[i], append i to ans.
# 4. Return ans.

# Time Complexity: O(n * m) - n is the number of words. For each word we
# scan up to m characters, where m is the length of that word, to check
# whether x is in it.
# Space Complexity: O(k) - k is the number of matching indices stored in
# ans. Extra variables besides the output use O(1) space.


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
        return ans
