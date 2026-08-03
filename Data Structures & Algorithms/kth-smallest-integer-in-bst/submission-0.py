# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count=0
        val = self.dfs(root, k)

        return val

    def dfs(self, root, k):
        if root is None:
            return

        left =  self.dfs(root.left, k)
        if left is not None:
            return left
        self.count+=1
        if self.count == k:
            val = root.val
            return val
        return self.dfs(root.right, k)
