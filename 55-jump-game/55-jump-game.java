class Solution {
    public boolean canJump(int[] nums) {
        if(nums.length == 1) return true;
        int[] waysToReach = new int[nums.length];
        waysToReach[0] = 1;
        for(int i = 0; i<nums.length - 1; i++){
            if(waysToReach[i] != 0){
                for(int j = nums[i]; j > 0; j--){
                    if(i + j < nums.length){
                        waysToReach[i+j] += 1;
                    }
                }
            }
        }
        return waysToReach[nums.length - 1] != 0;
        
    }
}