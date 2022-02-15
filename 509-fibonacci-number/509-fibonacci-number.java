class Solution {
    public int fib(int n) {
        int prev = 1;
        int prev_prev = 0;
        
        if (n== 0){
            return 0;
        }
        if (n== 1){
            return 1;
        }
        int cur = 2; 
        while (cur <= n){
            int next = prev + prev_prev;
            prev_prev = prev;
            prev = next;
            cur += 1;
            
        }
        
        return prev;
        
        
    }
}