# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.leafval(root,False)
    def leafval(self,root,value):
        if root == None:
            return 0
        if root.left==None and root.right==None and value:
            return root.val;
        ls = self.leafval(root.left,True)
        rs = self.leafval(root.right,False)
        return ls+rs