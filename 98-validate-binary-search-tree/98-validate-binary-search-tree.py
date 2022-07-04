# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
         
        
        def check(root,minV,maxV):
            if root is None:
                return True
            if root.val >= maxV or root.val <= minV:
                return False
            return check(root.left,minV,root.val) and check(root.right,root.val,maxV)
        
        
        return check(root,-math.inf,math.inf)
        
        
        
        
        
        
        
        
        
        
        