import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> counts = new HashSet<>();
        for (int num: nums){
            if (!counts.add(num)){
                return true;
            }
        }
        return false;
    }
}