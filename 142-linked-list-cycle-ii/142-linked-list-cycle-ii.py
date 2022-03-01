class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                break
        if fast == slow:
            return slow
        else:
            return None
        
        
        
        
        
        
#         # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if head is None or head.next is None:
#             return True
#         def reverse(head):
#             curr=head
#             prev=None
#             while curr!= None:
#                 temp=curr.next
#                 curr.next=prev
#                 prev=curr
#                 curr=temp
#             return prev
#         fast=head
#         slow=head
#         while fast is not None and fast.next is not None:
#             slow=slow.next
#             fast=fast.next.next
#         head_second_half=reverse(slow)
#         copy_head_second_half=head_second_half
#         while (head is not None and  head_second_half is not None):
#             if head.val != head_second_half.val:
#                 break
                
#             head=head.next
#             head_second_half.next 
#         if (head is not None or head_second_half is not None):
#             return True
#         else:
#             return False
        