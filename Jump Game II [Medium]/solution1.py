"""

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2

"""

"""

solution:

    This method is to keep finding the farthest move point and tract the move steps along the way.

    1. Initialize the move_step, farthest point (farthest) and current_end point (current_end)

    2. Loop the array from 1st element, and find the farthest movement

    3. If the farthest movement can reach the end of array, stop (Add the move step by 1) and report

    4. If pointer reach the current and it had not reach the true end, Update the current end to the farthest
       and Add the move step by 1

    5. Repeat step 3-4 untill the pointer reach the true end of array.

"""

nums = [2,3,1]

move_step = 0
farthest = 0
current_end = 0

for i in range(len(nums) - 1):

    # Find the farthest move
    farthest = max(farthest, i + nums[i])

    # If farthest move can reach the end of array, stop it and add the move step by 1
    if farthest >= len(nums) -1:
        move_step += 1
        break

    # If reach the current end, increase the move step and update the current end to the farthest.
    if i == current_end:
        current_end = farthest
        move_step += 1

print(move_step)