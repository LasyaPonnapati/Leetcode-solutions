# LeetCode 1903. Largest Odd Number in String
# You are given a string num representing a large integer. Return the
# largest-valued odd integer (as a string) that is a non-empty substring
# of num, or an empty string if no odd integer exists.

# Approach (brute force all substrings, keep the longest odd one):
# 1. Let i be the start index and j be the end index (inclusive).
# 2. For every substring num[i:j+1], check if it is odd.
# 3. A number is odd iff its last digit is odd, so check num[j].
#    Do not use int(substring) % 2: num can be up to 10^5 digits.
# 4. Among odd substrings, keep the longest. A longer digit string
#    (no extra leading zeros needed here) is a larger integer. The
#    longest odd substring is always the prefix through the last odd
#    digit, so the max length also gives the largest value.
# 5. If none are odd, ans stays "".

# Time Complexity: O(n^2) - n is the length of num. Two nested loops
# visit every start-end pair. Slicing to store ans is at most O(n)
# when we find a longer answer.
# Space Complexity: O(n) - ans holds one substring, at most n digits.


class Solution:
    def largestOddNumber(self, num: str) -> str:
        l = 0
        ans = ""
        for i in range(len(num)):
            for j in range(i, len(num)):
                if j - i + 1 > l and num[j] in "13579":
                    l = j - i + 1
                    ans = num[i : j + 1]
        return ans


# Approach (scan from the right for the last odd digit):
# Any odd substring must end on an odd digit. The longest one ends on
# the rightmost odd digit and starts at index 0.
# 1. Walk i from the last character toward the first.
# 2. When num[i] is odd, return num[0:i+1] (prefix through that digit).
# 3. If no digit is odd, return "".

# Time Complexity: O(n) - n is the length of num. Each index is checked
# at most once from right to left.
# Space Complexity: O(n) - the returned slice is at most n characters.
# The walk itself uses only the index i.


class SolutionFromEnd:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            if num[i] in "13579":
                return num[: i + 1]
        return ""


# Approach (walk left to right, remember the last odd index):
# Same idea as scanning from the right: the answer is the prefix
# through the rightmost odd digit. Here we find that index in one
# forward pass.
# 1. Set last = -1 to mean "no odd digit yet".
# 2. Walk i from 0 to n-1. Whenever num[i] is odd, set last = i.
# 3. After the loop, if last is still -1, return "". Else return
#    num[0:last+1].

# Time Complexity: O(n) - n is the length of num. One pass over all
# digits.
# Space Complexity: O(n) - the returned slice is at most n characters.
# The walk itself uses only last and i.


class SolutionLeftToRight:
    def largestOddNumber(self, num: str) -> str:
        last = -1
        for i in range(len(num)):
            if num[i] in "13579":
                last = i
        if last == -1:
            return ""
        return num[: last + 1]
