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
import java.io.*;
class Solution {
    private int maxCount; 
    private int freq;
    
    public int[] findFrequentTreeSum(TreeNode root) {
        Map<Integer, Integer> counts = new HashMap();
        dfs(root, counts);
        int[] ans = new int[freq];
        int idx = 0;
        for(Map.Entry<Integer, Integer> entry: counts.entrySet()){
            if(entry.getValue() == maxCount){
                ans[idx++] = entry.getKey();
            }
        }
        
        return ans;
        
        
    }
    
    public int dfs(TreeNode root, Map<Integer, Integer> counts){
        if(root != null){
            int res = root.val + dfs(root.left, counts) + dfs(root.right, counts);
            counts.put(res, counts.getOrDefault(res, 0) + 1);
             if(counts.get(res) == maxCount){
                freq++;
            }
            if(counts.get(res) > maxCount){
                freq = 1;
                maxCount = counts.get(res);
            }
            return res;
        }
        return 0;
    }
}