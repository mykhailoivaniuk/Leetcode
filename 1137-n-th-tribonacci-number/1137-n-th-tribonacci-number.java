class Solution {
    public int tribonacci(int n) {
        int zeroth = 0;
        int first = 1;
        int second = 1;
        
        if (n==0){
            return 0;
        }
        
        if (n==1){
            return 1;
        }
        
        if (n==2){
            return 1;
        }
        
        int cur = 2;
        while (cur < n) {
            int next = zeroth + first + second;
            zeroth = first;
            first = second;
            second = next;
            cur += 1;
        }
        
        return second;
    }
}