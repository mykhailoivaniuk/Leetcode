/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isValidBST(TreeNode root) {
       return helper(root, null, null);
    }
    
    public boolean helper(TreeNode node, Integer max, Integer min) {
        if(node == null) return true;
        if((min != null && node.val <= min) || (max != null && node.val >= max)) {
            return false;
        }
        return helper(node.left, node.val, min) &&
                helper(node.right, max, node.val);
    }
    
    
}