# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack=[root]
        height_map={None:0}

        flag=True
        while stack:
            node=stack[-1]

            if node.left and node.left not in height_map:
                stack.append(node.left)
            elif node.right and node.right not in height_map:
                stack.append(node.right)
            else:
                node=stack.pop()

                leftHeight=height_map[node.left]
                rightHeight=height_map[node.right]

                if abs(leftHeight-rightHeight)>1:
                    return False

                height_map[node]=1+max(rightHeight, leftHeight)
        return True
            



