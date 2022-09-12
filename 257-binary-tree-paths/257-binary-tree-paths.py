# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
         
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        ans=[]
        def dfs(root,path):
            
            if root.left is None and root.right is None:
                ans.append(path)
                
            if root.left:
                dfs(root.left,path+"->"+str(root.left.val))
                
            if root.right:
                
                dfs(root.right,path+"->"+str(root.right.val))
                
        dfs(root,str(root.val))
        return ans
    
               
    
    