# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 16:08
@Author:     wz
@File:       旋转图像.py
@Decs:
"""

"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
matrix:
[1,2,3]     [7,4,1]
[4,5,6] ->  [8,5,2]
[7,8,9]     [9,6,3]

可以先把矩阵转置，再进行翻转
[1,2,3]     [1,4,7]     [7,4,1]
[4,5,6] ->  [2,5,8] ->  [8,5,2]
[7,8,9]     [3,6,9]     [9,6,3]
"""

class Solution:
    def function(self, matrix):

        # 转置
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 每行反转
        for i in range(len(matrix)):
            left, right = 0, len(matrix[i]) - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
        return matrix

if __name__ == "__main__":
    s = Solution()
    print(s.function([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
