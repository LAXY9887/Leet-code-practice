'''

Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

'''

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: list[int]) -> TreeNode:

    def findMid(ilist:list):
            length = len(ilist)
            mid = int(len(ilist)/2)
            if length % 2 == 0:
                mid -= 1
            return mid

    def subTree(ilist:list):
        if len(ilist) == 0:
            return None
        mid = findMid(ilist)
        sublist1 = ilist[:mid]
        sublist2 = ilist[mid+1:]
        root = TreeNode(ilist[mid],left=subTree(sublist1),right=subTree(sublist2))
        return root
    
    return subTree(nums)

inputl = [1,3]

root = sortedArrayToBST(inputl)

print("root = ",root.val)
print("left = ",root.left)
print("right = ",root.right)