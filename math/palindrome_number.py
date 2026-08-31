# LeetCode 9. Palindrome Number
# Given an integer num, return True if num reads the same forward and
# backward (a palindrome), otherwise return False.

# Approach:
# 1. Negative numbers are not palindromes (the minus sign is only on one side).
# 2. Save the original number, then reverse the digits the same way as
#    reverse integer: start result at 0, take num % 10, then
#    result = result * 10 + digit, and drop that digit with num // 10.
# 3. The number is a palindrome if original equals the reversed value.

# Time Complexity: O(d) - we walk through each of the d digits once.
# Space Complexity: O(1) - only a few integer variables are used.


class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False

        original = num
        result = 0

        while num > 0:
            digit = num % 10
            num = num // 10
            result = result * 10 + digit

        return original == result
