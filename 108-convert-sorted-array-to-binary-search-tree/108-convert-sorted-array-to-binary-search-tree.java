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
    private int[] nums;
    
    public TreeNode sortedArrayToBST(int[] nums) { 
        this.nums = nums;
        return helper(0, nums.length - 1);
    }

    public TreeNode helper(int left, int right) {
        if(left > right) return null;
        int rootIdx = (left + right) / 2;
        return new TreeNode(nums[rootIdx],
                           helper(left, rootIdx -1),
                           helper(rootIdx + 1, right));
    }
}
