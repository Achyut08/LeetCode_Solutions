# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result=[]
        if root is None:
            return result
        queue=deque([])
        queue.append(root)
        while len(queue) != 0:
            level_size=len(queue)
            for i in range(level_size):
                current=queue.popleft()
                if (i==level_size-1):
                    result.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
        return result
