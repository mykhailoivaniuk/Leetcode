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
import java.util.Stack;

class Solution {
    public void flatten(TreeNode root) {
        if(root == null) return;
        Deque<TreeNode> stack = new ArrayDeque<>();
        stack.push(root);
        while(!stack.isEmpty()){ 
            TreeNode cur = stack.pop();
            if(cur.right != null) stack.push(cur.right);
            if(cur.left != null) stack.push(cur.left);
            if(!stack.isEmpty()) cur.right = stack.peek();
            cur.left = null;
        }
    }
}