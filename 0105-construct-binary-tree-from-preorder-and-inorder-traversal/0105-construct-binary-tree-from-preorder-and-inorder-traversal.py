# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        
        if not preorder or not inorder:
            return None
        
        
        root=TreeNode(preorder[0])
        
        mid=inorder.index(preorder[0])
        
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        
        return root
        
        
        


 


















        # def recur(l,m,h):            ## wrong soltn think why

        #     if l>h:
        #         return None


        #     nodevalue=inorder[m]

        #     root=TreeNode(nodevalue)

        #     root.left=recur(l,(l+m-1)//2,m-1)

        #     root.right=recur(m+1,(m+1+h)//2,h)

        #     return root

        # return recur(0,inorder.index(preorder[0]),len(inorder)-1)    