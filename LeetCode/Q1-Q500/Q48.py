class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        touch = [[0] * n for _ in range(n)]
        
        for i in range(n) :
            for j in range(n) :
                if not touch[n-1-j][i]:
                    matrix[i][j],matrix[n-1-j][i]=matrix[n-1-j][i],matrix[i][j]
                    touch[i][j]=1