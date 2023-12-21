'''

Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def show2End(self):
         while self != None:
              print(self.val)
              self = self.next

def deleteDuplicates(head: ListNode) -> ListNode:
    
    dummy = head

    # check current val and next val
    while head and head.next:
        
        current = head.val
        next_val = head.next.val

        # if dup , conect next to next-next node (skip the dup one)
        if next_val == current:
            head.next = head.next.next
            
            # If dup, dont do 'head = head.next' below.
            # Because we want the pointer to stay at the position. 
            
            continue # if true, skip the code below.

        head = head.next

    return dummy


# This is a array [1,1,2,3]
head1 = ListNode(1,ListNode(1,ListNode(2,ListNode(3))))

# This is a array [1,1,2,3,3,4]
head2 = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4))))))

# This is a array [1,1,1,1]
head3 = ListNode(1,ListNode(1,ListNode(1,ListNode(1))))

ans = deleteDuplicates(head3)

print(">=Report=<")
ans.show2End()
