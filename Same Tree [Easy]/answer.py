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

策略是:
1. 檢查當前兩個 node 是否皆為空, 如果是則視作兩個 tree 相同
2. 若其中一個為空,另一個不是,則兩個tree不同
3. 若當前兩個 node 的值不同,則兩個tree不同
4. 疊代左邊以及右邊, 直到位末端, 檢測以上 3 點
5. 以 AND 邏輯串聯兩個疊代結果, 如果兩端都能通過則代表兩個 tree 相同

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: TreeNode, q: TreeNode) -> bool:

    if not p and not q:
        return True
    
    if not p or not q or p.val != q.val:
        return False
    
    return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

p = TreeNode(1,left=TreeNode(1),right=None)
q = TreeNode(1,left=None,right=TreeNode(1))

print("Is same? --> ", isSameTree(p,q))