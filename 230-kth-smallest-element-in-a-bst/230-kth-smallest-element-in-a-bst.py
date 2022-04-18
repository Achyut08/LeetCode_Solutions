# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sort = []  
        def inOrderTrav(node):
            if node.left:
                inOrderTrav(node.left)
            sort.append(node.val)
            if node.right:
                inOrderTrav(node.right)
            return
        inOrderTrav(root)
        return sort[k-1]