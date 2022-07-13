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
import java.util.*;
class Solution {
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> rightSide = new ArrayList<>();
        Deque<TreeNode> queue = new ArrayDeque<>();
        if(root == null) return rightSide;
        
        queue.add(root);
        while(queue.size() != 0){
            int levelSize = queue.size();
            for(int i = 0; i < levelSize; i++){
                TreeNode curNode = queue.pop();
                if(curNode.left != null) queue.add(curNode.left);
                if(curNode.right != null) queue.add(curNode.right);
                if(i == levelSize - 1) rightSide.add(curNode.val);
            }
            
        }
        
        return rightSide;
        
    }
}