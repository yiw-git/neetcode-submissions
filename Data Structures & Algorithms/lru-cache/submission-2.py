class Node:
    def __init__(self, key=0, val=0):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes={}# value is nodes and they are actually linked together
        self.cap=capacity

        self.head=Node()
        self.tail=Node()
        self.head.next=self.tail
        self.tail.prev=self.head
        #head<==>last
    def _remove(self,node):
        #here, we already know which node it is, remvoe B
        #head<->A<->B<->C<->tail
        #head, tail are dummy nodes
        #node.prev refers to the node before B
        node.prev.next=node.next#A.next->C
        node.next.prev=node.prev#C.prev->A
    def _add_recent(self,node):
        #head<->A<->B<->C<->tail
        last=self.tail.prev #last is C
        last.next=node #C->D
        node.prev=last
        node.next=self.tail
        self.tail.prev=node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node=self.nodes[key]
        self._remove(node)#first pick it up and then add to the end
        self._add_recent(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node=self.nodes[key]
            node.val=value #update the value of the node
            self._remove(node)
            self._add_recent(node)
            return
        else:
            #time to create the new node and put it to cahe
            node=Node(key, value) #create the node instance
            self.nodes[key]=node #add to dictionary, key-> node, for fast lookup
            self._add_recent(node)#add to linked list

            #at put, consider the len
            if len(self.nodes)>self.cap:
                oldest=self.head.next
                self._remove(oldest)
                del self.nodes[oldest.key]


