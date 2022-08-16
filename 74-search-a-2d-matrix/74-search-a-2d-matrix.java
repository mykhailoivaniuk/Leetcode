class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int rowIdx = findRowIdx(matrix, target);
        return findInRow(matrix, rowIdx, target);
    }
    public boolean findInRow(int[][] matrix, int rowIdx, int target){
        if(rowIdx >= matrix.length) return false;
        int start = 0, end = matrix[rowIdx].length - 1;
        while(start <= end){
            int mid = start + (end - start)/2;
            if(matrix[rowIdx][mid] > target) end = mid - 1;
            if(matrix[rowIdx][mid] < target) start = mid + 1;
            if(matrix[rowIdx][mid] == target) return true;
        }
        return false;
    }
    public int findRowIdx(int[][] matrix, int target) {
        int start = 0, end = matrix.length - 1;
        int lastRowIdx = matrix[0].length - 1;
        int mid = 0;
        while(start <= end){
            mid = start + (end - start) / 2;
            if(matrix[mid][lastRowIdx] > target) end = mid - 1;
            if(matrix[mid][lastRowIdx] < target) start = mid + 1;
            if(matrix[mid][lastRowIdx] == target) return mid;
        }
        return start;
    }
}