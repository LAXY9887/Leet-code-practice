'''

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

'''

'''

策略:
1. 建立兩個array, 分別代表左右兩半
2. 將左半邊tree從最末端開始將值加入 left array (lf)
   將右半邊tree從最末端開始將值加入 right array (lr)
   若當前node為空則記錄None, 
   
   否則以對稱的順序加入節點的數值:
        左側加入順序 --> 1. 下一個左側節點 2. 下一個右側節點 3. 當前節點的數值
        右側加入順序 --> 1. 下一個右側節點 2. 下一個左側節點 3. 當前節點的數值

3. 最終比較 lf 是否等於 lr

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:

        def helper(l: list, node: TreeNode, direction: str):
            if not node: 
                l.append(None)
                return
            if direction == 'L':
                helper(l,node.left,"L")
                helper(l,node.right,"L")
                l.append(node.val)
            elif direction == 'R':
                helper(l,node.right,"R")
                helper(l,node.left,"R")
                l.append(node.val)

        lf = []
        lr = []

        helper(lf,root.left,'L')
        helper(lr,root.right,'R')

        return lf == lr


# root = [1,2,2,3,4,4,3]
root = TreeNode(1,left=TreeNode(2,left=TreeNode(3),right=TreeNode(4)),right=TreeNode(2,left=TreeNode(4),right=TreeNode(3)))

print(isSymmetric(root))