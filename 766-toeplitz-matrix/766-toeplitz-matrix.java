class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for(int i = matrix.length - 1; i > -1; i--){
            if(!checkDiagonal(matrix, i, 0)){
                return false;
            }
        }
        for(int j = 1; j<matrix[0].length; j++){
            if(!checkDiagonal(matrix, 0, j)) return false;
        }
        return true;
    }
    
    public boolean checkDiagonal(int[][] matrix, int row, int col){
        if(row >= matrix.length || col >= matrix[0].length){
            return true;
        }
        int diagVal = matrix[row][col];
        while(row < matrix.length && col< matrix[0].length){
            if(matrix[row][col] != diagVal) return false;
            row++;
            col++;
        }
        return true;
    }
}