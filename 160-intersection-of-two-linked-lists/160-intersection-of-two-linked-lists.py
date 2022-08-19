# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n1,n2 = 0,0
        temp1 =headA
        temp2 = headB
        while(temp1):
            n1 += 1
            temp1 = temp1.next
        while(temp2):
            n2 += 1
            temp2 = temp2.next
        temp1 =headA
        temp2 = headB
        ab = abs(n1-n2)
        if n1>n2:
            while(ab>0):
                temp1 = temp1.next
                ab -= 1
        else:
            while(ab>0):
                temp2 = temp2.next
                ab -= 1
        while(temp1 != temp2):
            temp1 = temp1.next
            temp2 = temp2.next
        
        return temp1
                
                