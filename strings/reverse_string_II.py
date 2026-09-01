# LeetCode 541. Reverse String II
# Given a string s and an integer k, reverse the first k characters for
# every 2k characters counting from the start of the string.
# - If there are fewer than k characters left, reverse all of them.
# - If there are fewer than 2k but at least k characters, reverse the
#   first k and leave the rest as they are.

# Approach (pointer + slice reverse):
# 1. Start at index num = 0.
# 2. While num is still inside the string, reverse the next k characters
#    (or whatever is left if the tail is shorter than k).
# 3. Keep the rest of the string the same. Build a new string:
#    prefix + reversed chunk + suffix.
# 4. Jump num forward by 2k so the next k characters (the ones we skip)
#    stay in original order.
# 5. Repeat until num is past the end.

# Time Complexity: O(n) - n is the length of s. Each character is copied
# a constant number of times as we rebuild the string in 2k-sized steps.
# Space Complexity: O(n) - each step builds a new string of length n, and
# Python strings cannot be reversed in place.


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        num = 0
        while num < len(s):
            s = s[:num] + s[num:num + k][::-1] + s[num + k:]
            num += 2 * k
        return s
