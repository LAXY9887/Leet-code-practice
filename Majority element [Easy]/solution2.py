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

    1. Loop through the numeric array, record the different numbers in a dict (dp) and calculate its counts.

    2. If a number is exist in the dp, increase its counts by 1.

    3. Each step, check if the current number's count is grater than half of array length.

    4. If a number count > half of array length, stop and report.

"""

# Input
nums = [2,2,1,1,1,1,1]

# A dict to record the number of each different element
dp = {}

# Loop through the array
for each in nums:

    # Add the new element if it is not in the dp, set the count to 0
    if each not in dp:
        dp[each] = 0
    
    # Increase the element's count
    dp[each] += 1

    # Check if an element's count is grater than half of array length
    if dp[each] > len(nums) // 2:
        print(each)
        break