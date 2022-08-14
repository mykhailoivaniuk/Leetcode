/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode prev = null;
        Deque<TreeNode> stack = new ArrayDeque<>();
        while(true){
            while(root != null) {
                stack.push(root);
                root = root.left;
            }
            if(stack.isEmpty()) return null;
            root = stack.pop();
            if(p.equals(prev)) return root;
            prev = root;
            root = root.right;
        }        
    }
}