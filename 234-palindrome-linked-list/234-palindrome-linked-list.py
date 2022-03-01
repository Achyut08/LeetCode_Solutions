class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=None 
        while slow:
            next=slow.next
            slow.next=temp
            temp=slow
            slow=next
        while temp:
            if temp.val != head.val:
                return False
            temp=temp.next
            head=head.next
        return True