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
    
    public int[] findFrequentTreeSum(TreeNode root) {
        List<Integer> res = new ArrayList();
        Map<Integer, Integer> counts = new HashMap();
        int rootVal = dfs(root, counts);
        for(Map.Entry<Integer, Integer> entry: counts.entrySet()){
            if(entry.getValue() == maxCount) res.add(entry.getKey());
        }
        
        return res.stream().mapToInt(i -> i).toArray();
        
        
    }
    
    public int dfs(TreeNode root, Map<Integer, Integer> counts){
        if(root != null){
            int res = root.val + dfs(root.left, counts) + dfs(root.right, counts);
            counts.put(res, counts.getOrDefault(res, 0) + 1);
            maxCount = Math.max(maxCount, counts.get(res));
            return res;
        }
        return 0;
    }
}