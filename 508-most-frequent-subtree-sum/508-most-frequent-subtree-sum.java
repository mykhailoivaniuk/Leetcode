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
    public int[] findFrequentTreeSum(TreeNode root) {
        List<Integer> res = new ArrayList();
        Map<Integer, Integer> counts = new HashMap();
        int rootVal = dfs(root, counts);
        System.out.println(counts.toString());
        int curMax = Integer.MIN_VALUE;
        for(Map.Entry<Integer, Integer> entry: counts.entrySet()){
            int val = entry.getKey();
            int count = entry.getValue();
            curMax = Math.max(curMax, count);
        }
        
        for(Map.Entry<Integer, Integer> entry: counts.entrySet()){
            int count = entry.getValue();
            if(count == curMax) res.add(entry.getKey());
        }
        int[] ans = res.stream().mapToInt(i -> i).toArray();
        return ans;
        
        
    }
    
    public int dfs(TreeNode root, Map<Integer, Integer> counts){
        if(root != null){
            int res = root.val + dfs(root.left, counts) + dfs(root.right, counts);
            counts.merge(res, 1, Integer::sum);
            return res;
        }
        return 0;
    }
}