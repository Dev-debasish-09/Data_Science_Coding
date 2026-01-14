class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_set = set()
        col_set = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
        for i in range(n):
            for j in range(m):
                if i in row_set or j in col_set:
                    matrix[i][j]=0
