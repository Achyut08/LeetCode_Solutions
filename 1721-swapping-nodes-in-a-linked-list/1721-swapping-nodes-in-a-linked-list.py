# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        slow = fast = n1= head
        for _ in range(k-1):
            fast = fast.next
        n1 = fast
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        n2 = slow
        temp = n1.val
        n1.val = n2.val
        n2.val = temp
        return head