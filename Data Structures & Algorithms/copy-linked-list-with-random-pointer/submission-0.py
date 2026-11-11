"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy={None:None}

        cur=head
        while cur:
            #here is to use copy
            copy=Node(cur.val)
            oldToCopy[cur]=copy #哎，是不是说这个字典的 key-value 中的 key 就是 cur 这个 node 呢？
            cur=cur.next
        cur=head
        while cur:
            copy=oldToCopy[cur]
            copy.next=oldToCopy[cur.next]
            copy.random=oldToCopy[cur.random]
            cur=cur.next
        return oldToCopy[head]

        
