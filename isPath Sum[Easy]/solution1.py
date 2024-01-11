'''

Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.


'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, targetSum: int) -> bool:
    
    def helper(node,sum):
            
        # If it is an empty node, return False
        if not node: return False

        # If it is a leaf node and the node value is equal to residule of target, return true
        if not node.left and not node.right and sum == node.val:
            return True

        # If node value is not equal to residule of target, ask left and right node to do the check. 
        return helper(node.left,sum-node.val) or helper(node.right,sum-node.val)


    return helper(root, targetSum)

root = TreeNode(2,left=TreeNode(1,left=TreeNode(1)),right=TreeNode(3,right=TreeNode(7)))

ans = hasPathSum(root,4)
print(ans)