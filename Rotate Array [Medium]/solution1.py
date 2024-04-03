"""

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]


Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

"""
solution:

    1. pop the first item of nums and append it to the last position (rotate rigth)

    2. calculate the number of right rotating (t) is qual to left rotating k times

    3. if length of nums > k, t = len(nums) - k

       if length of nums > k, t = len(nums) - k%len(nums)

       [example, k = 4, nums = [1,2,3]. Rotating 4 times is equivlant to Rotating once.]

    4. No matter len(nums) is grater or smaller than k, k%len(nums) is always correct, so just do k%len(nums).

"""

nums = [1,2,3]
k = 4

for i in range(len(nums) - k%len(nums)):
    nums.append(nums.pop(0))

print(nums)