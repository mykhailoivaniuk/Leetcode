class Solution {
    public int searchInsert(int[] nums, int target) {
        int leftIdx = 0, rightIdx = nums.length;
        int mid = 0;
        if(target > nums[nums.length -1]) return nums.length;
        while(leftIdx < rightIdx) {
            mid = (leftIdx + rightIdx) / 2;
            if(nums[mid] > target){
                rightIdx = mid;
            }
            if(nums[mid] < target){
                leftIdx = mid + 1;
            }
            else if(nums[mid] == target){
                return mid;
            }
        }
        if(nums[mid]< target) return mid + 1;
        return mid;
    }
}