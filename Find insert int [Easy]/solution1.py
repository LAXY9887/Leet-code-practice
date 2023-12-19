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
    
    count = 0
    
    while count < len(nums):
        
        if nums[count] < target: 
            count += 1
        else:
            break

    return count

nums = [1,2,3,5,6]
target = 4

ans = searchInsert(nums=nums,target=target)
print(ans)