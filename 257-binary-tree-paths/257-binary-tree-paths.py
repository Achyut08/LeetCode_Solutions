# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, node, path, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append("{}{}".format(path, node.val))
        self.dfs(node.left, "{}{}->".format(path, node.val), res)
        self.dfs(node.right, "{}{}->".format(path, node.val), res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
