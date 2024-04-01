"""

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

"""

"""

solution:

 create 2 pointer, slow pointer move 1 node each step, fast pointer move 2 node each step

 if the link list is cyclic, the fast one will eventually catch the slow one inside the loop

 if there is an end of list, fast pointer will reach None.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

def isCyclic(node):

    # Create 2 pointer start at head node
    faster = node
    slower = node

    
    while faster:

        if faster == slower:
            return True
        
        # Start moving pointer
        faster = faster.next.next
        slower = slower.next

    return False

print(isCyclic(head))