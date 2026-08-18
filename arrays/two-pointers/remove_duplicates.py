# LeetCode 26. Remove Duplicates from Sorted Array
# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
# such that each unique element appears only once. The relative order of the elements should
# be kept the same. Return the number of unique elements.

# Approach (two-pointer):
# 1. x points to the last unique position written (starts at 1 because nums[0] is always unique).
# 2. y scans the array from index 1 onward.
# 3. If nums[y] equals nums[y-1], skip it by moving y forward.
# 4. If nums[y] is a new unique value, write it at nums[x], then move both x and y forward.
# 5. Return x, which is the count of unique elements.

# Time Complexity: O(n) - y scans the array once, and x moves at most n times.
# Space Complexity: O(1) - the removal is done in-place with only two pointers.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x,y=1,1
        while y<len(nums):
            if nums[y]==nums[y-1]:
                y+=1
            else:
                nums[x]=nums[y]
                x+=1
                y+=1
        return x
