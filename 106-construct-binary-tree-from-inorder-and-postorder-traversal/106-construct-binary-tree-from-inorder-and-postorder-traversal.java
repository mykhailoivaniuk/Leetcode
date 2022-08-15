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
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        Map<Integer, Integer> valToIdx = new HashMap<>();
        for(int i = 0; i< inorder.length; i++){
            valToIdx.put(inorder[i], i);
        }
        return helper(postorder.length -1, 0, inorder.length - 1, inorder, postorder, valToIdx);
    }
    public TreeNode helper(int poRoot, int inStart, int inEnd, int[] inOrder, int[] postOrder, Map<Integer, Integer> idxs) {
        if(inStart > inEnd || poRoot >= postOrder.length || poRoot < 0) return null;
        int inIdx = idxs.get(postOrder[poRoot]);
        TreeNode root = new TreeNode(postOrder[poRoot]);
        root.right = helper(poRoot - 1, inIdx + 1, inEnd, inOrder, postOrder, idxs);
        root.left = helper(poRoot - inEnd + inIdx - 1, inStart, inIdx - 1, inOrder, postOrder, idxs);
        return root;
    }
}