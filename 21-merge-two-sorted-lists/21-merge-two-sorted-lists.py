# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2==None:
            return l1
        head = l1
        if l1.val>l2.val:
            head = l2
            l2 = l2.next
        else:
            l1 = l1.next
        curr = head
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1 != None:
            curr.next = l1
        if l2 != None:
            curr.next = l2
        return head