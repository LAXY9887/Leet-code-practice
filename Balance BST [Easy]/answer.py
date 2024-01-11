'''

Given a binary tree, determine if it is height-balanced.

Input: root = [3,9,20,null,null,15,7]
Output: true

Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Input: root = []
Output: true

'''

'''

 策略: 計算 left 和 right 的長度, 比較他們的差異是否大於 1 

 helper function:
 (base condition) 當 node 為 None 時 回傳 0
 (Recurssion) left = helper(left) 直到末端節點
              right = helper(right) 直到末端節點
 (判斷狀況) 當 left, right 的差異 > 1 時, 回傳 -1
 (判斷狀況) 當 left 或 right = -1 時, 回傳 -1 (因為他在其他跌代過程中已經有 left 和 right 的差異 > 1 的情形)
 (Return) 回傳 max(left,right) + 1 , 當遇到(base condition)時則為 0 + 1 = 1 只回傳最長的路徑
          並且隨著跌代過程累加, 除非發現 left, right 的差異 > 1

 判斷 helper(root) 是否為 >= 0 (而不是-1 如果是, 則代表left, right 的差異 > 1)


'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# This is a high balance 
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20,left=TreeNode(15),right=TreeNode(7))

def calculateHeight(node):

    if not node: return 0

    left = calculateHeight(node.left)
    right = calculateHeight(node.right)

    if left < 0 or right < 0 or abs(left - right) > 1:
        return -1

    return max(left,right) +1

def isBalanced(root: TreeNode) -> bool:
    return calculateHeight(root) >= 0

print(isBalanced(root))