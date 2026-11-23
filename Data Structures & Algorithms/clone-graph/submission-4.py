"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #dictionary, key is the original node and value if the copied node
        #each node has val and neighbors
        if node is None:
            return None
        dic1={}
        
        def dfs(node):
            if node in dic1:
                return dic1[node] #so it i connected to the neighbors
            copied=Node(node.val)
            dic1[node]=copied #save it before visiting neighbors
            for neighbor in node.neighbors:
                copied.neighbors.append(dfs(neighbor))
            return copied
        dfs(node)
        return dic1[node]

