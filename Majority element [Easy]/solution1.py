"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

"""

solution:

    1. sort the array, since it is numeric array.

    2. Find the middle number, the majority (more than half) one must cover the middle position.

"""

# Input
nums = [2,2,1,1,1,1,1]

# Sort it
nums.sort()

# Get the length
n = len(nums)

# Show the middle number
print(nums[n // 2])