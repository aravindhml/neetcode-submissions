# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        out = root 
        root = self.insert(root,val)

        return root
    def insert(self,root,val):

        if root is None:
            t = TreeNode()
            t.val = val
            return t
            
        
        if val < root.val:
            root.left = self.insert(root.left,val)
        
        elif val > root.val:
            root.right = self.insert(root.right,val)

        return root