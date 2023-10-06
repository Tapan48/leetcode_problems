# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        
        res=float("inf")
        prev=None
        def inorder(root):   ## recursive soltn
            nonlocal prev,res
            if not(root):
                return 
            
            
            inorder(root.left)
            
            if prev:
                res=min(res,root.val-prev.val)
                
            prev=root  
            inorder(root.right)
        inorder(root)
        return res
            
            
            
            
            
            
            
            
          
        inorder(root)
        return res
            
            
            
            
          
              
               
                
                
        inorder(root)
        return x
        
#         arr=[]
#         def inorder(root):    ### tc o(n) sc o(n)         
            
#             if not(root):
#                 return 
            
            
            
#             inorder(root.left)
#             arr.append(root.val)
#             inorder(root.right)
        
#         inorder(root)
#         res=arr[len(arr)-1]
#         for i in range(len(arr)-1):
              
#             diff=arr[i+1]-arr[i]
#             res=min(res,diff)
            
#         return res        
                
        