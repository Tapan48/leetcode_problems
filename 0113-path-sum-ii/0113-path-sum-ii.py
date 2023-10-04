# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        
        
        res=[]
        
        def dfs(root,cursum,arr):
            
            if not(root):
                return 
            
            cursum+=root.val
            arr.append(root.val)
            
            if not(root.left)and not(root.right) and cursum==targetSum:
                
                res.append(arr.copy())
                # return
        
                
                
            
            
            
            
            
                                  
            
            
            dfs(root.left,cursum,arr)
            
            
            dfs(root.right,cursum,arr)
            arr.pop()
            
        
        dfs(root,0,[])
        return res
        