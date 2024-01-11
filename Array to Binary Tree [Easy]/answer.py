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

    def subTree(ilist:list):

        # calculate list length
        length = len(ilist)

        # if sub list is empty, return None
        if length == 0:
            return None
        
        # 向下整除2
        mid = length//2

        # 製作 sublist
        sublist1 = ilist[:mid]
        sublist2 = ilist[mid+1:]

        # 回傳節點 val = 中位數, 左邊 = 遞歸左邊sublist, 右邊 = 遞歸右邊sublist
        # 直到 sublist 為空為止
        return TreeNode(ilist[mid],left=subTree(sublist1),right=subTree(sublist2))
    
    return subTree(nums)

inputl = [1,3]

root = sortedArrayToBST(inputl)

print("root = ",root.val)
print("left = ",root.left)
print("right = ",root.right)