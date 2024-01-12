# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        
        arr1=[]
        arr2=[]
        
        def dfs(root,tree1):
            
            if not root:
                return 
            
            
            
            if not(root.left)and not(root.right):
                if tree1:
                    arr1.append(root.val)
                else:
                    arr2.append(root.val)
            
            dfs(root.left,tree1)
            dfs(root.right,tree1)
            
        dfs(root1,True)  
        dfs(root2,False)
        if arr1==arr2:
            return True
        
        return False
            
                
            
            