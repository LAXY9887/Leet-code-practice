'''

This script is an example of creating a binary tree.

'''

class TreeNode:

    # 建構式, 一個Node包含一個整數, 左邊和右邊節點
    def __init__(self, val:int = None, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    # 插入一個值
    def insert(self,new_val):
        
        # 如果比自身小,則往左邊走
        if new_val <= self.val:
            
            # 如果沒有左邊節點,則新增一個左邊節點, val = new_val
            if not self.left:
                self.left = TreeNode(new_val)

            # 如果已有左邊節點,則使左側節點做 insert(new_val), 直到最末端節點為止
            else:
                self.left.insert(new_val)
        
        # 如果比自身大,則往右邊走
        else:

            # 如果沒有右邊節點,則新增一個右邊節點, val = new_val
            if not self.right:
                self.right = TreeNode(new_val)

            # 如果已有右邊節點,則使右側節點做 insert(new_val), 直到最末端節點為止
            else:
                self.right.insert(new_val)

    # 檢查數字是否在Tree當中
    def Contain(self,check_val):
        
        # 如果數值(check_val)等於自身數值, 則回傳True
        if check_val == self.val:
            return True
        
        # 如果數值(check_val)小於自身數值, 則往左邊尋找, 直到最末端節點為止
        if check_val < self.val:
            if self.left:
                return self.left.Contain(check_val)
            else:
                return False # 沒有左邊的話則回傳False
            
        # 如果數值(check_val)大於自身數值, 則往右邊尋找, 直到最末端節點為止
        elif check_val > self.val:
            if self.right:
                return self.right.Contain(check_val)
            else:
                return False # 沒有右邊的話則回傳False

    # 印出 node 底下整個 Tree
    def print_inorder(self):

        # 如果有左邊節點,則使左邊節點執行print_inorder(), 直到最末端節點為止
        if self.left:
            self.left.print_inorder()
        
        # 如果沒有左邊節點, 則印出自身的值
        print(self.val)

        # 如果有右邊節點,則使右邊節點執行print_inorder(), 直到最末端節點為止
        if self.right:
            self.right.print_inorder()

# An array of int to construct a tree stucture
vals = [1,3,5,7,9,11,29,50]

# Create a tree root
root = TreeNode(vals[0])

# Add vals into tree
for each in vals[1:]:
    root.insert(each)

# print the tree inorder
root.print_inorder()

# Find some vals in the tree
print(root.Contain(9))
print(root.Contain(100))