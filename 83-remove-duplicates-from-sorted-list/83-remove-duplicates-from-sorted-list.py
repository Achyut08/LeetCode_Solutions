# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr:
            while curr.next != None and curr.next.val == curr.val:
                curr.next = curr.next.next   # skip duplicated node
            curr = curr.next
        return head
        
        
        
        
        
        
        