# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                el = q.popleft()
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
                
                level.append(el.val)
            result.append(level)
        
        return result


        