# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels=[]
        que=collections.deque()
        que.append(root)

        while que:
            qlen=len(que)
            level=[]
            while qlen>0:
                node=que.popleft()
                qlen-=1
                if node:
                    level.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if level:
                levels.append(level)
        return levels





