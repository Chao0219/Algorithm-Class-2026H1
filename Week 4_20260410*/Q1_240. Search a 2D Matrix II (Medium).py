class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find min and max in the matrix, and then "guess" where the number would be.
        # m is column ; n is row
        m = len(matrix)  ; n = len(matrix[0])
        min_val = matrix[0][0]; max_val = matrix[m-1][n-1]
        # guess the position

        if min_val == max_val:
            if target == min_val:
                return True

        for i in range(m):
            if target >= matrix[i][0] and target <= matrix[i][n-1] :
                mid = matrix[i][(n-1)//2]
                if target > mid:
                    for j in range((n//2)-1,(n)):
                        if target == matrix[i][j]:
                            return True
                else:
                    for j in range(0, (n//2)+1):
                        if target == matrix[i][j]:
                            return True

