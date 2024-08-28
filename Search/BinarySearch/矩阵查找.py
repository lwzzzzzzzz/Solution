# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/25 0:33
@Author:     wz
@File:       矩阵查找.py
@Decs:
"""

"""
在行列都是单调递增的矩阵中寻找指定target
输入：matrix：
    [[1, 3, 5, 7]
    ,[10,11,16,20]
    ,[23,30,34,60]]
target = 3
输出：true
"""


class Solution:
    def function(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            i, j = mid // n, mid % n  # 核心在于将二分查找的数组下标映射成矩阵二维下标
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return True

        return False


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    s = Solution()
    print(s.function(matrix, target))
