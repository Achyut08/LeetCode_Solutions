# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        max_value = 0
        lt = self.maxDepth(root.left)
        rt = self.maxDepth(root.right)
        
        return 1 + max(lt,rt)
        