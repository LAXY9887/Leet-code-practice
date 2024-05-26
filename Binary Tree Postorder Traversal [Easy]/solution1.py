"""

Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        
        collection = []

        def helper(node):
            
            # Stop if current node is empty
            if not node:
                return

            # Call left first
            helper(node.left)

            # Then call right
            helper(node.right)

            # Finally add itself
            collection.append(node.val)

        # It will become postorder
        helper(root)

        return collection
    

## Test Case
root = TreeNode(1,left=None,right=TreeNode(2,left=TreeNode(3)))
soln = Solution()

# Solution
ans = soln.postorderTraversal(root=root)
print(ans)