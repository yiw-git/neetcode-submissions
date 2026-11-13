# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
        if root:
            tovisit=deque([root])
        while tovisit:
            node=tovisit.popleft()
            
            if p.val<node.val and q.val<node.val:
                if node.left:
                    tovisit.append(node.left)
                else:
                    return False
            elif p.val>node.val and q.val>node.val:
                if node.right:
                    tovisit.append(node.right)
                else:
                    return False
            else:
                return node
             
                

        