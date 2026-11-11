# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack1=[root]
        stack_sub=[]
        while stack1:
            node=stack1.pop()
            if not node:
                continue
            if node.val==subRoot.val:
                results=self.sameTree(node, subRoot)
                if results==True:
                    return True
            stack1.append(node.left)
            stack1.append(node.right)
        return False

    def sameTree(self, root: Optional[TreeNode], subRoot:Optional[TreeNode])->bool:
        st=[(root, subRoot)]
        while st:
            node1, node2=st.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val==node2.val:
                st.append((node1.left, node2.left))
                st.append((node1.right, node2.right))
            else:
                return False
            
            
        return True




        