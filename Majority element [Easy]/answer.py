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

solution (Moore's Voting Algorithm):

    1. Create 2 varibles, candidate and count

    2. Loop through the array, if count == 0, update the candidate to the new number

    3. During the looping, if it meets the same number as candidate, add the count by 1

       if it meets a different one, minus the count by 1,

    4. Once the count become 0, , update the candidate to the new number

    5. Finally, the majority number will survive.

"""

# Input
nums = [2,2,1,1,1,1,1]

# Inititalize count = 0
count = 0

for each in nums:

    # If count = 0, update the candidate
    if count == 0:
        candidate = each

    # If candidate is the same, add count
    if candidate == each:
        count += 1

    # if candidate is different, minus count
    else:
        count -= 1

print(candidate)