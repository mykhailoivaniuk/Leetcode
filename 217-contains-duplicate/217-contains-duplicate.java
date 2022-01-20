import java.util.HashMap;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        HashMap<Integer, Integer> counts = new HashMap<>();
        for (int num: nums){
            if (counts.containsKey(num)){
                counts.put(num,counts.get(num)+1);
                if (counts.get(num) == 2){
                    return true;
                }
            }
            else {
                counts.put(num,1);
            }
        }
        return false;
    }
}