# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        def solve(root,val):
            if root == None:
                return True
            if (root.val != val):
                return False
            left = solve(root.left,val)
            right = solve(root.right,val)
            
            return left & right
        return solve(root,root.val)