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
    public boolean hasPathSum(TreeNode root, int targetSum) {
        return helper(root, targetSum);
    }
    
    public boolean helper(TreeNode node, int cur_sum) {
        if(node == null){
            return false;
        }
        if(node.right == null && node.left == null && cur_sum - node.val == 0){
            return true;
        }
        return helper(node.right, cur_sum - node.val) || 
            helper(node.left, cur_sum - node.val);
    }
}