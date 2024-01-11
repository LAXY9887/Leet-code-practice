
'''

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

'''

'''

策略: 計算 left 和 right 的長度, 比較他們的差異是否大於 1 

 helper function:
 (base condition) 當 node 為 None 時 回傳 0
 (Recurssion) left = helper(left) 直到末端節點
              right = helper(right) 直到末端節點
 (判斷狀況) 如果下一層左右兩個節點都存在 node.left and node.right, 回傳 min(left, right) 
 (判斷狀況) 如果下一層只有單邊的節點, 則回傳 max(left, right)
            ※ 此時如果回傳 min 值, 則會被空的那一邊影響到, 反而計算不到完整的連續長度 !
            例題1: root = [-9,-3,2,null,4,4,0,-6,null,-5]
            例題2: root = [2,null,3,null,4,null,5,null,6]

 判斷 helper(root) 是否為 >= 0 (而不是-1 如果是, 則代表left, right 的差異 > 1)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def countHeight(node):

            if not node: return 0

            left = countHeight(node.left) +1

            right =  countHeight(node.right) +1

            if left >= 2 and right >= 2:
                return min(left,right)
            
            return max(left,right)
        
        if not root: return 0

        return countHeight(root)