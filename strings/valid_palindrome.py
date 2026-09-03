# LeetCode 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters
# into lowercase letters and removing all non-alphanumeric characters,
# it reads the same forward and backward.
# Alphanumeric characters include letters and numbers.

# Approach (build cleaned string, then compare with reverse):
# 1. Walk through each character in s.
# 2. Skip anything that is not a letter or a digit.
# 3. Lowercase the remaining characters and append them to out.
# 4. The string is a palindrome if out equals out reversed.

# Time Complexity: O(n) - n is the length of s. We scan s once to build
# out, then reverse out (also O(n)) for the comparison.
# Space Complexity: O(n) - out stores up to n cleaned characters, and
# slicing out[::-1] creates another string of the same length.


class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ""
        for i in s:
            if not i.isalnum():
                continue
            out += i.lower()
        if out == out[::-1]:
            return True
        return False


# Approach (two pointers on the original string):
# Building out and then reversing it (or even two-pointering on out)
# still uses extra space for the cleaned copy. A better version never
# builds out at all.
# 1. Put left at the start of s and right at the end.
# 2. Move left forward until it hits an alphanumeric character.
# 3. Move right backward until it hits an alphanumeric character.
# 4. Compare those two characters in lowercase. If they differ, it is
#    not a palindrome.
# 5. If they match, step both pointers inward and repeat.
# 6. If the pointers meet or cross, every pair matched.

# Time Complexity: O(n) - each index is visited at most once as left
# only moves right and right only moves left.
# Space Complexity: O(1) - only a few pointers and character checks;
# no extra string is created.


class SolutionTwoPointers:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
