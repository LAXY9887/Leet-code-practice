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

# Iteration method (Depth first search)

# Create a queue for looping
queue = [root]

# Create a list to store vals
collection = []

while queue:

    # Take "the last" item in queue
    node = queue.pop()
    collection.append(node.val)

    # if right or left exist, Add next nodes to queue for process 
    # Add right into the list first, since pop() will take the last one in list
    # To make sure the process order is root -> left -> right !
    for next_nodes in [node.right,node.left]:
        if next_nodes:
            queue.append(next_nodes)

print(collection)
