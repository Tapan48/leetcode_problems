# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            
        """   
        x=[] 
        def inorder(root):   ## recursive soltn
            
            if root:
                
                
                inorder(root.left)
                x.append(root.val)
                inorder(root.right)
            return None    
            
          
              
               
                
                
        inorder(root)
        return x
    """
        """ 
        res=[]
        stack=[]
        
        
        while root or stack:     ## iterative soltn
            
            while root:
                stack.append(root)
                root=root.left
                
            while stack:
                node=stack.pop()
                res.append(node.val)
                if node.right:
                    root=node.right
                    break
                else:
                    root=None
        return res
    
    """
    
    
        res=[]
        stack=[]
        
        
        while root or stack:     ## iterative soltn
            
            while root:
                stack.append(root)
                root=root.left
                
            root=stack.pop()
            res.append(root.val)
            root=root.right
            
        return res            
                    
                    
                    
        
        
      