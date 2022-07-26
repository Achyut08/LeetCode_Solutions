# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def dfs(node):
            if node is None:
                return 0
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            self.ans = max(self.ans, node.val+left+right)
            return max(left, right)+node.val
        self.ans = -(9**31)
        dfs(root)
        return self.ans
    
    
    
#      def maxSum(root):
#         nonlocal maxi
#         if root==None:
#             return 0
#         leftSum= max(0,maxSum(root.left))
#         rightSum= max(0,maxSum(root.right))
        
#         maxi=max(maxi,leftSum+rightSum + root.val)
        
#         return root.val + max(leftSum,rightSum)
    
    
#     maxi=-(9**31)
#     maxSum(root)
#     return maxi