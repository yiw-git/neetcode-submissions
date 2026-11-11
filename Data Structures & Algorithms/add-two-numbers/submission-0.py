# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        digit=1
        sum1=0
        while l1:
            sum1+=l1.val*digit
            digit*=10
            l1=l1.next

        digit=1
        sum2=0
        while l2:
            sum2+=l2.val*digit
            digit*=10
            l2=l2.next

        sum3=sum1+sum2
        dummy=ListNode()
        cur=dummy
        i=len(str(sum3))-1
        while i>=0:
            num=int(str(sum3)[i])
            i-=1
            cur.next=ListNode(num)
            #cur.val=num
            cur=cur.next

        return dummy.next




