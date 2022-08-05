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
class BSTIterator {
    
    private ArrayDeque<TreeNode> nodes = new ArrayDeque<>();
    private TreeNode pointer;
    public BSTIterator(TreeNode root) {
        nodes.add(new TreeNode(Integer.MIN_VALUE, null, root));
        populate(nodes, root);
    }
    
    public void populate(Deque<TreeNode> nodes, TreeNode root) {
        if(root == null) return;
        populate(nodes, root.left);
        nodes.add(root);
        populate(nodes, root.right);
    }
    public int next() {
        nodes.pop();
        return nodes.peekFirst().val;
    }
    
    public boolean hasNext() {
        return nodes.size() > 1;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */