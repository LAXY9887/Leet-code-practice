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
 
    Imagine there is a car with gasolin, and travel along with nums array,

    once it move a step forward, the gas will decrease by 1.

    However, if it meets a number grater than current gas, it will be refill to the number and keep going

    If the car can drive through the array, it means the jump is avaliable.

    if gas is less than 0 during traveling, it means the jump is not avaliable.

"""

nums = [0]

gas = 0

canJump = True

for each in nums:

    if gas < 0:
        canJump = False
        break

    elif each > gas:
        gas = each

    gas -= 1

print(canJump)