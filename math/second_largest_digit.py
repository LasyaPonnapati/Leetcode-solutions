# LeetCode 1796. Second Largest Digit in a String
# Given a mixed string s of digits and letters, return the second largest
# distinct digit in s. If there is no second largest digit, return -1.

# Approach:
# 1. Track the largest digit (f_max) and the second largest digit (s_max).
#    Start both at -1 so we do not pretend 0 already appeared.
# 2. Walk each character. Skip it if it is not a digit.
# 3. Convert the digit character to an int.
# 4. If it is bigger than f_max, the old f_max becomes s_max, and this
#    digit becomes f_max.
# 5. Else if it is smaller than f_max but bigger than s_max, it becomes
#    the new s_max. Equal to f_max is ignored (we need distinct digits).
# 6. Return s_max (-1 if we never found a second distinct digit).

# Time Complexity: O(n) - one pass over the string of length n.
# Space Complexity: O(1) - only two integer variables are stored.


class Solution:
    def secondHighest(self, s: str) -> int:
        f_max = -1
        s_max = -1

        for i in s:
            if not i.isdigit():
                continue

            digit = int(i)

            if digit > f_max:
                s_max = f_max
                f_max = digit
            elif digit > s_max and digit != f_max:
                s_max = digit

        return s_max
