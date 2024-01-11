# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        
        def dfs(root):
            
            if not(root):
                return 0
            
            if root.val>=low and root.val<=high:
                
                return root.val+dfs(root.left)+dfs(root.right)
            
            elif root.val<low:
                return dfs(root.right)
            
            else:
                return dfs(root.left)
        return dfs(root)    
        