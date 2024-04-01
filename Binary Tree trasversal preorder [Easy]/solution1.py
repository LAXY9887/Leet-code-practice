"""

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,2,3]

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1,right=TreeNode(2,left=TreeNode(3)))

# Recursive solution
collection = []
def preorder_trasversal(node):
    
    if node:
        collection.append(node.val)

        if node.left:
            collection.append(preorder_trasversal(node.left))

        if node.right:
            collection.append(preorder_trasversal(node.right))

preorder_trasversal(root)
while None in collection:
    collection.remove(None)
print(collection)