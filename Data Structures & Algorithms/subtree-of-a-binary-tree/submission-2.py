# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            if node.val==subRoot.val:
                if self.sameTree(node, subRoot):
                    return True

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return False

    def sameTree(self, root:Optional[TreeNode], subRoot:Optional[TreeNode])->Bool:
        stack=[(root, subRoot)]
        while stack:
            node1, node2=stack.pop()
            if node1 and node2 and node1.val==node2.val:
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False
        return True




            

        