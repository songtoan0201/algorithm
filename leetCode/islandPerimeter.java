class Solution {
    public int islandPerimeter(int[][] arr) {
        int count = 0;
        for(int i = 0; i < arr.length; i++) {
            for(int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == 1) {
                    count += 4;
                    if (j < arr.length - 1 && arr[i][j+1] == 1)
                        count--;
                    if (j > 0 && arr[i][j-1] == 1)
                        count--;
                    if (i < arr[i].length - 1 && arr[i+1][j] == 1)
                        count--;
                    if (i > 0 && arr[i-1][j] == 1)
                        count--;
                }
            }
        }
        return count;
    }
}