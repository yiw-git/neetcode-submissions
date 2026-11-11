# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length=0
        cur=head
        while cur:
            cur=cur.next
            length+=1

        idx=length-n
        if idx==0:
            return head.next

        point=head
        while idx>0:
            prev=point
            latter=point.next
            point=latter
            idx-=1
        prev.next=latter.next
        return head




