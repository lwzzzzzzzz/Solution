# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 15:36
@Author:     wz
@File:       矩阵置零.py
@Decs:
"""


class Solution:
    """
        给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0。
        利用两个flag数组，来标识该行或列是否需要置零
    """

    def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = [False] * len(matrix)
        col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if row[i] or col[j]:
                    matrix[i][j] = 0
        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
