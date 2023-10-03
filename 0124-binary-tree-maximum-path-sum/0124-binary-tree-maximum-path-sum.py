# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        
        
        
        ans = float('-inf') 
        def dfs(root):
            nonlocal ans
            
            if not(root):
                return 0
            
            # if not(root.left)and not(root.right):
            #     return root.val
            
            
            
            
            
            ### without splitting
            leftcall=dfs(root.left)
            rightcall=dfs(root.right)
            res=root.val+max(leftcall,rightcall,0)
            
            ### with splitting
            ans=max(ans,root.val+leftcall+rightcall,res)
            
            return res        ####  returns without splitting max path sum for that node
        dfs(root)
        return ans
            
            
            
            
        
        
        
        
        
        