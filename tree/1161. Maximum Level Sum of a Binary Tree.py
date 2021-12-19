# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        bfs=[]
        maxi_sum=0
        if root is None:
            return maxi_sum
        queue=deque([])
        queue.append(root)
        while len(queue) != 0:
            sum1=[]
            level_order=len(queue)
            for i in range(level_order):
                current=queue.popleft()
                sum1.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            bfs.append(sum(sum1))
        return bfs.index(max(bfs)) + 1
                
            
        
