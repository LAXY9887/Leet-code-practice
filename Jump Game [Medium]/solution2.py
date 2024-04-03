"""

You are given an integer array nums. You are initially positioned at the array's first index, 

and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
Its maximum jump length is 0, which makes it impossible to reach the last index.
 
"""

"""

solution:
 
    This method is to keep moving goal from the end of array.

    1. Initially, the goal_idx is at len(nums), and we should check the previous postition (i) to see whether it can 
       achieve the goal.

    2. If it can (i + nums[i] >= goal_idx), the goal is replcae by the position i, because one can achieve i, can achieve goal.

    3. Repeat step 1 & 2 untill the goal reach to the head of array.

       if finally the goal is equal to 0 (first element of array), it means jump is avaliable, 

       otherwise, the jump is not avaliable.

"""

nums = [2,3,1,1,4]

# The goal is start from last index
goal_idx = len(nums) - 1

# Loop through the array backward from last 2 position to check.
for i in range(len(nums)-2, -1, -1):

    # Check if the current position can achieve the goal.
    if i + nums[i] >= goal_idx:

        # if so, update the goal position.
        goal_idx = i


if goal_idx == 0:
    print(True)

else:
    print(False)

