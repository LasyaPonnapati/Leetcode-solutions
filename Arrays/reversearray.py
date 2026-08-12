# LeetCode 344. Reverse String
# Write a function that reverses a string. The input string is given as a list of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Two-pointer approach: x starts at 0, y starts at len(s) - 1.
# Swap s[x] and s[y], then move x forward and y backward until they meet in the middle.

# Time Complexity: O(n) - each character is swapped once, so we visit n/2 pairs.
# Space Complexity: O(1) - only two pointer variables are used, swap happens in-place.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        x = 0
        y = len(s) - 1
        while x < y:
            s[x], s[y] = s[y], s[x]
            x += 1
            y -= 1
