class Solution {
    public int climbStairs(int n) {
        if (n == 1){
            return 1;
        }
        
        if (n == 2) {
            return 2;
        }
        
        int[] possible_combos = new int[n];
        possible_combos[0] = 1;
        possible_combos[1] = 2;
        
        for (int i = 2; i < n; i++) {
            possible_combos[i] = possible_combos[i-1] + possible_combos[i-2];
        }
        
        return possible_combos[n-1];
        
    }
}