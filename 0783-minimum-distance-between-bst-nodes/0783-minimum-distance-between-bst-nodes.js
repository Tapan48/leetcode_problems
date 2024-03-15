/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function(root) {
    
    let res=Infinity;
    
    let prev=null;
    
    
    function inorder(root){
        
        if(!root){
            
            return
        }
        
        inorder(root.left)
        
        if (prev){
            
            res=Math.min(res,root.val-prev.val)
        }
        prev=root;
        inorder(root.right)
    }
    inorder(root)
    return res
    
    
    
};