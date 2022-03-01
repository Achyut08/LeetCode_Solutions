# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        even = head.next
        odd = head
        evenhead = even
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = evenhead
        return head
    
    
    
    
    
    
    
    
    
    
    # if head:
        #     odd_tail, cur = head, head.next
        #     while cur and cur.next:
        #         even_head = odd_tail.next
        #         odd_tail.next = cur.next
        #         odd_tail = odd_tail.next
        #         cur.next = odd_tail.next
        #         odd_tail.next = even_head
        #         cur = cur.next
        # return head