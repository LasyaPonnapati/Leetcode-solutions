# LeetCode 1221. Split a String in Balanced Strings
# Balanced strings are those that have an equal quantity of 'L' and 'R'
# characters. Given a balanced string s, split it into some number of
# substrings such that:
# - Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.

# Approach 1 (count L and R, split when they match):
# 1. Walk the string one character at a time.
# 2. If the character is 'R', add 1 to cr. If it is 'L', add 1 to cl.
# 3. When both counts are greater than 0 and equal, this piece is
#    balanced. Add 1 to the answer and reset cr and cl to 0 so the next
#    piece starts fresh.
# 4. Return how many balanced pieces we found.

# Time Complexity: O(n) - n is the length of s. We visit each character
# once.
# Space Complexity: O(1) - only a few integer counters are stored.


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        cr = 0
        cl = 0
        for i in s:
            if i == "R":
                cr += 1
            else:
                cl += 1
            if cr > 0 and cl > 0 and cr == cl:
                count += 1
                cr = 0
                cl = 0
        return count


# Approach 2 (one running balance):
# You do not need two counters. Keep one number called balance.
# 1. 'R' adds 1, 'L' subtracts 1 (or the other way around).
# 2. When balance is 0, you have seen the same number of L and R since
#    the last split, so this piece is balanced. Add 1 to count.
# 3. You never reset balance because 0 already means "start a new piece".
# Same greedy idea as Approach 1, just fewer variables.
# cr > 0 and cl > 0 in Approach 1 is extra: after you process a
# character, cr == cl can only happen when both are at least 1.

# Time Complexity: O(n) - still one pass over s. You cannot do better
# than this because every character must be read.
# Space Complexity: O(1) - only two integers: balance and count.


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balance = 0
        for i in s:
            if i == "R":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                count += 1
        return count
