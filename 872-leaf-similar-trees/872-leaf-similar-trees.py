# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def solve(root):
            if root is None:
                return []
            if root.left == None and root.right == None:
                return [root.val]
            return solve(root.left) + solve(root.right)
        list_root1 = solve(root1)
        list_root2 = solve(root2)
        if list_root1 == list_root2:
            return True
        return False
            
            