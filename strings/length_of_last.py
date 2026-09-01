# LeetCode 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of
# the last word in the string. A word is a maximal substring consisting
# of non-space characters only.

# Approach 1 (strip + reset count):
# 1. Strip leading and trailing spaces.
# 2. Walk each character. If it is a letter, add 1 to count.
# 3. If it is a space, reset count to 0 so the next word starts from 0.
# 4. After the loop, count is the length of the last word.

# Time Complexity: O(n) - strip and the loop each scan the string once.
# Space Complexity: O(n) - strip() builds a new string of length up to n.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        l = s.strip()
        for i in l:
            count += 1
            if i == ' ':
                count = 0
        return count


# Approach 2 (two while loops, no extra string):
# 1. Walk the original string with index i.
# 2. If s[i] is a letter, add 1 to count and move i forward.
# 3. If s[i] is a space, skip all spaces with the inner loop.
# 4. After skipping spaces, if the next character is a letter, a new
#    word is starting, so reset count to 0. The outer loop will count it.
# 5. Check i < len(s) before reading s[i] so we never go past the end.

# Time Complexity: O(n) - each index is visited at most once.
# Space Complexity: O(1) - only count and i are stored.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        i = 0
        while i < len(s):
            if s[i] != ' ':
                count += 1
                i += 1
            while i < len(s) and s[i] == ' ':
                i += 1
                if i < len(s) and s[i] != ' ':
                    count = 0
        return count


# Approach 3 (walk from the end):
# 1. Start at the last character. Skip trailing spaces.
# 2. Then count letters until you hit a space or the start of the string.
# 3. That count is the last word. Earlier words are never visited.

# Time Complexity: O(n) - in the worst case we still scan the whole string
# (for example one word, or many trailing spaces). We often stop earlier.
# Space Complexity: O(1) - only i and count are stored.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        count = 0
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1
        return count
