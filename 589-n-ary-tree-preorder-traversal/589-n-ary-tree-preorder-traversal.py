"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        solution = []
        if root == None:
            return []
        def preorder1(root):
            if root == None:
                return 
            solution.append(root.val)
            for child in root.children:
                preorder1(child)
        preorder1(root)
        return solution