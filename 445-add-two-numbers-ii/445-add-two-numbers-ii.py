# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            current=head
            nexp=None
            prep=None
            while(current!=None):
                nexp=current.next
                current.next=prep
                prep=current
                current=nexp
            head=prep
            return head
        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry //= 10
        return  reverse(dummy.next)
        