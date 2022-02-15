class Solution {
    public int minCostClimbingStairs(int[] cost) {
        
        int size = cost.length;
        if (size <= 2) {
            return Math.min(cost[0],cost[1]);
        }
        
        for (int i = 2; i < size; i++) {
            
            cost[i] += Math.min(cost[i-1],cost[i-2]);
            
        }
        
        // System.out.println(Arrays.toString(cost));
        return Math.min(cost[size-1],cost[size-2]);
        
        
        
    }
}