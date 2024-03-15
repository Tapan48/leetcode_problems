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
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    
    
    
    function dfs(root,cursum){
        
        
        if (!root){
            return  false
        }
        
        cursum+=root.val
        
        if (!root.left &&  !root.right){
            
            return (cursum===targetSum) 
        }
        
        return dfs(root.left,cursum)||dfs(root.right,cursum)
    }
    
    
    return dfs(root,0)
};