# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        
        q=deque()
        q.append(root)
        res=[]
        
        cnt=0
        
        while q :
            
            qlen=len(q)
            
            level=[]
            
            
            
            
            for i in range(qlen):
                
                node=q.popleft()
                if node:
                    level.append(node.val)
                
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                
            if cnt%2:
                res.append(level[::-1])
            else:
                res.append(level) if level else res
                
            cnt+=1  
        return res   
                    
                
                
                
                
                
                
            
            
        