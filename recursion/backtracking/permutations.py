# LeetCode 2094. Finding 3-Digit Even Numbers
# Given an array digits (each value is a digit 0-9, duplicates allowed),
# return a sorted list of all unique 3-digit even numbers you can form
# by using three digits from the array. Numbers cannot have a leading zero.

# Approach:
# 1. Use backtracking to build a number digit by digit (curr) from the
#    unused digits (remaining).
# 2. At each step, skip a digit value if we already tried it in this
#    position (used set) so we do not generate the same number twice
#    from duplicate digits.
# 3. Choose a digit, append it, recurse with that digit removed from
#    remaining, then pop it (backtrack) to try the next choice.
# 4. Base case: when curr has 3 digits, keep it if the first digit is
#    not 0 and the last digit is even. Store the integer in a set.
# 5. Return the set as a sorted list.

# Time Complexity: O(n^3) - we build 3-digit sequences, so at most
# n * (n - 1) * (n - 2) paths, and each step copies remaining (O(n)).
# Sorting the unique answers is smaller than that.
# Space Complexity: O(n) - recursion depth is 3, plus copies of remaining
# and the set of unique 3-digit numbers (at most a few hundred).

from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = set()

        def backtrack(curr, remaining):
            if len(curr) == 3:
                if curr[0] != 0 and curr[2] % 2 == 0:
                    result.add(curr[0] * 100 + curr[1] * 10 + curr[2])
                return

            used = set()

            for i in range(len(remaining)):
                if remaining[i] in used:
                    continue

                used.add(remaining[i])

                curr.append(remaining[i])
                backtrack(curr, remaining[:i] + remaining[i + 1 :])
                curr.pop()

        backtrack([], digits)

        return sorted(result)
