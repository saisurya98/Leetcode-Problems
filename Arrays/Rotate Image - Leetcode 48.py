class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 90 Degree rotation : First do the transpose of matrix
        # Then do mirror image of matrix column wise ( vertically)
        # TC-O(N2)
        # SC-O(1)
        #Transpose
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # print(matrix)
        # vertical mirror image
        for i in range(n):
            for j in range((n//2)):
                matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
        return matrix
