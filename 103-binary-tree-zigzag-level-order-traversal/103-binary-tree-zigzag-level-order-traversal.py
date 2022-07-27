# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        flag = 0
        ans = []
        queue = deque([])
        if root is None:
            return ans
        queue.append(root)
        
        while len(queue) != 0:
            flag += 1
            level = len(queue)
            res = []

            for i in range(level):
                current = queue.popleft()
                res.append(current.val)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            if flag%2:
                ans.append(res)
            else:
                ans.append(res[::-1])
            
        return ans
  

 # if root is None:
#                 return 
#             q=deque()
#             q.append(root)
#             count=0
#             while q:
#                 count+=1
#                 path=[]
#                 size=len(q)
#                 for _ in range(size):
#                     node=q.popleft()
#                     path+=[node.val]
#                     if node.left:
#                         q.append(node.left)
#                     if node.right:
#                         q.append(node.right)
#                 if count%2:
#                     res.append(path)
#                 else:
#                     res.append(path[::-1])
#             return res
#         res=[]
#         return helper(root,res)