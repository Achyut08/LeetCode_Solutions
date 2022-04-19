class Solution:
    def correctBstUtil(self,root,first,middle,last,prev):
        if(root):
		    # Recur for the left sub tree
            self.correctBstUtil(root.left, first, middle, last, prev)
            
			# If this is the first violation, mark these
            # two nodes as 'first and 'middle'
			
            if(prev[0] and root.val < prev[0].val):
                if(not first[0]):
                    first[0] = prev[0]
                    middle[0] = root
                else:
				    
					# If this is the second violation,
                   # mark this node as last
                    last[0]=root
            prev[0]=root
            
			# Recur for the right subtree
            self.correctBstUtil(root.right, first, middle, last, prev)
            
			# A function to fix a given BST where
			# two nodes are swapped. This function
			# uses correctBSTUtil() to find out two
			# nodes and swaps the nodes to fix the BST
			
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
		# Followed four lines just for forming
		# an array with only index 0 filled
		# with None and we will update it accordingly.
		# we made it null so that we can fill
		# node data in them
		
        first = [None]
        middle = [None]
        last = [None]
        prev = [None]
        
        self.correctBstUtil(root, first, middle,last, prev)
        
        if(first[0] and last[0]):
            first[0].val,last[0].val=(last[0].val,first[0].val)
        elif(first[0] and middle[0]):
            first[0].val,middle[0].val=(middle[0].val,first[0].val)