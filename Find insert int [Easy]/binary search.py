'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''

def searchInsert(nums: list[int], target: int) -> int:

    p_left = 0
    p_right = len(nums) -1

    while p_left <= p_right:

        p_mid = int((p_left + p_right) / 2)

        if target > nums[p_mid]:
            p_left = p_mid +1
        elif target < nums[p_mid]:
            p_right = p_mid -1
        else:
            return p_mid
    
    return p_left

nums = [1,2,3,5,6,7]
target = 4

ans = searchInsert(nums,target)
print(ans)