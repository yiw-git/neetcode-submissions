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
        nodecopy={None:None}
        cur=head
        while cur:
            nodecopy[cur]=Node(cur.val)
            cur=cur.next
        
        for old, new in nodecopy.items():
            if old is None:
                continue
            new.next=nodecopy[old.next]
            new.random=nodecopy[old.random]
        return nodecopy[head]

