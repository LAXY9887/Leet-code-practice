'''

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:

        if not root:
            return 0

        def collectNode(current):
            
            count = 1

            if current.left and current.right: 
                lefter = collectNode(current.left) +1 
                righter = collectNode(current.right) +1
                return max(lefter,righter)

            if current.right and not current.left:
                count += collectNode(current.right)

            if current.left and not current.right:
                count += collectNode(current.left)

            if not current.left and not current.right:
                return count

            return count

        return collectNode(root)
    

# Test node
root = TreeNode(3,left=TreeNode(9),right=TreeNode(20,left=TreeNode(15),right=TreeNode(7)))

maxLength = maxDepth(root)

print("Max depth = ", maxLength)