# LeetCode 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit range
# [-2^31, 2^31 - 1], then return 0.

# Approach:
# 1. Remember the sign, then work with the absolute value of num.
# 2. Build the reversed number as an integer: start result at 0.
#    Each step, take the last digit (num % 10), then
#    result = result * 10 + digit, and drop that digit with num // 10.
# 3. Put the sign back on result.
# 4. If result is outside the 32-bit range, return 0.

# Time Complexity: O(d) - we process each of the d digits once
# (d is at most 10 for a 32-bit integer).
# Space Complexity: O(1) - only a few integer variables are used.


class Solution:
    def reverse(self, num: int) -> int:
        sign = -1 if num < 0 else 1
        num = abs(num)
        result = 0

        while num > 0:
            digit = num % 10
            num = num // 10
            result = result * 10 + digit

        result = sign * result
        if result < -(2**31) or result > 2**31 - 1:
            return 0
        return result
