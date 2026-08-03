# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        res = self.dfs(root,root.val)

        return res
    

    def dfs(self,node,maxi):
        if not node:
            return 0
        res =1 if maxi<=node.val else 0
        maxi = max(maxi,node.val)
        res+= self.dfs(node.left,maxi)
        res+= self.dfs(node.right,maxi)

        return res