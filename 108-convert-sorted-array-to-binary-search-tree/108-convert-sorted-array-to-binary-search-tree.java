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
    public TreeNode sortedArrayToBST(int[] nums) { 
        if(nums.length >= 3) {
            int rootIdx = nums.length / 2;
            return new TreeNode(nums[rootIdx],
                               sortedArrayToBST(Arrays.copyOfRange(nums, 0, rootIdx)), 
                               sortedArrayToBST(Arrays.copyOfRange(nums, rootIdx + 1, nums.length)));
        }
        if(nums.length >= 2){
            return new TreeNode(nums[0], null, new TreeNode(nums[1]));
        }
        return new TreeNode(nums[0]);
        
    }
}