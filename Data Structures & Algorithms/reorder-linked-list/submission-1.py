# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=head.next
        slow=head

        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        second=slow.next
        slow.next=None

        #head is second, 
        prev, cur =None, second
        while cur:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            
        second=prev
        first=head

        while second:
            temp1=first.next
            temp2=second.next
            first.next=second
            second.next=temp1
            first=temp1
            second=temp2

      
            

        

        
        
        