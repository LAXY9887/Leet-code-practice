"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:

    # 若其中一個list不存在則回傳另一個
    if not list1 and not list2:
            return list1
    if not list1 or not list2:
        return list1 if not list2 else list2

    # 創立一個暫時ListNode: cur; 原始 node: dum
    cur = ListNode()
    dum = cur

    # 當兩個ListNode皆不為None時
    while list1 and list2:
        #比較大小,將cur的下一個串接到數字小的Node
        if list1.val < list2.val:
            cur.next = list1

            # 更新list至下一個
            list1 = list1.next

            # 更新cur至下一個 (dum仍是第一個node)
            cur = cur.next

        #比較大小,將cur的下一個串接到數字小的Node
        else:
            cur.next = list2

            # 更新list至下一個
            list2 = list2.next

            # 更新cur至下一個 (dum仍是第一個node)
            cur = cur.next

        # 檢查list是否為None, 將cur的下一個串接到當前還存在的list
        if list1:
            cur.next = list1
        elif list2:
            cur.next = list2

    # 回傳原始的(第一個node)
    return dum.next

# 輸入初始(第一個)node印出所有接下來的值
def reportNode(init:ListNode):
    print(init.val)
    while init.next != None:
        init = init.next
        print(init.val)

# Demo, list1 = [0,2,4]
list1 = ListNode(0)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

# Demo, list2 = [1,3]
list2 = ListNode(1)
list2.next = ListNode(3)

# 執行
ans = mergeTwoLists(list1,list2)

# 印出答案
reportNode(ans)