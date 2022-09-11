# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        
        x=[]
        def posttrav(root):
            
            if root:
                
                posttrav(root.left)
                posttrav(root.right)
                x.append(root.val)
            return None
        
        
        
        posttrav(root)
        
        return x