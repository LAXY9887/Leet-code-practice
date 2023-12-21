'''

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:

    def helper(node : TreeNode):
        # Stop this function if node is None.
        if not node: return

        # 這將會去到左邊最底部
        helper(node.left)
        # 將數值加入res中
        res.append(node.val)
        # 這將會去到每個分支的, 右邊最底部
        helper(node.right)


    # To store values
    res = []

    # Inorder traverse
    helper(root)

    return res

# This is a tree
root = TreeNode(1)
root.left = None
root.right = TreeNode(2,left=TreeNode(3))

ans = inorderTraversal(root)
print(ans)