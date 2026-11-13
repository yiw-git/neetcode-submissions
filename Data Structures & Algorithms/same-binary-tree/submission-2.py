# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        
        stack=[(p,q)]

        while stack:
            node1, node2=stack.pop()
            if not node1 and not node2:
                continue
            if (not node1 and node2) or (not node2 and node1) or node1.val !=node2.val:
                return False
            elif node1.val==node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            else:
                return False
        return True
        






