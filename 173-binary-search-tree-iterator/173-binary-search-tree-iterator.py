class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        def inorder(node):
            if not node:
                return []
            else:
                return inorder(node.left) + [node] + inorder(node.right)
        
        self.nodes = inorder(root)
        self.pt = -1
        self.length = len(self.nodes)

        return None

    def next(self) -> int:
        
        self.pt += 1
        return self.nodes[self.pt].val

    def hasNext(self) -> bool:

        return self.pt < self.length - 1