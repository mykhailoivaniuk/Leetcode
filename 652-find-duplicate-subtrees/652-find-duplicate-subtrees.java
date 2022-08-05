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
import java.lang.StringBuilder;

class Solution {
    private Map<String, Integer> seen = new HashMap<>();
    private List<TreeNode> result = new ArrayList<>();
    
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        findHelper(root);    
        return result;
    }
    
    public String findHelper(TreeNode root) {
        if(root == null) return "";
        String curr = "(" + root.val + " "+ findHelper(root.left) + " "+ findHelper(root.right);
        seen.merge(curr, 1, Integer::sum);
        if(seen.get(curr) == 2) result.add(root);
        return curr;
        
        
        
    }
}