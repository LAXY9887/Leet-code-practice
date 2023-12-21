'''

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false

'''
'''

策略是將 p 和 q 的值記錄到2個列表中, 最後比較兩個列表是否相同

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:
        
        pl = []
        ql = []

        def helper(l:list, node: TreeNode):
            if not node : 
                l.append(None)
                return
            l.append(node.val)
            helper(l,node.left)
            helper(l,node.right)
        
        helper(pl,p)
        helper(ql,q)

        print("q = ", ql)
        print("p = ", pl)

        return pl == ql

p = TreeNode(1,left=TreeNode(1),right=None)
q = TreeNode(1,left=None,right=TreeNode(1))

print("Is same? --> ", isSameTree(p,q))