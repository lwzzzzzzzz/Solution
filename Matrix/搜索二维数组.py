# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 1:02
@Author:     wz
@File:       搜索二维数组.py
@Decs:
"""

"""
1. 行or列内部有序
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
输入：matrix = 
    [[1, 4, 7, 11, 15]
    ,[2, 5, 8, 12, 19]
    ,[3, 6, 9, 16, 22]
    ,[10,13,14,17, 24]
    ,[18,21,23,26,30]]
target = 8
输出：true 索引为[1,2]

思路：此时因为整个矩阵并不是完全有序，则不满足二分查找的前提，所以我们此时以最后一列为基准，大于则往后面行查找，小于则往前面列查找。
时间复杂度 O(m+n)

2. 当整个矩阵完全有序，则矩阵按照顺序严格有序
输入：matrix = 
    [[1, 3, 5, 7]
    ,[10,11,16,20]
    ,[23,30,34,60]]
则此时可以把矩阵仍然看成一个长为m*n的有序list，left=0; right=m*n-1，每次正常更新mid，但都把mid映射到矩阵的下标上 i=mid//n, j=mid%n，
按照matrix[i][j]取数与目标值进行比较
时间复杂度 O(log(m*n))
"""


class Solution:
    def grid_search_matrix(self, matrix, target):
        """
            行列内部有序：以最后一列为基准，大于则往后面行查找，小于则往前面列查找。
        """
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        while i < m - 1 and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return [i, j]
        return False

    def binary_search_matrix(self, matrix, target):
        """
            整个数组有序：把矩阵仍然看成一个长为m*n的有序list，left=0; right=m*n-1，每次正常更新mid，在矩阵里取数比较
        """
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = left + (right - left) // 2
            i, j = mid // n, mid % n  # 核心在比较元素时，将二分查找的数组下标mid映射成矩阵二维下标取数比较
            if matrix[i][j] < target:
                left = mid + 1
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                return [i, j]

        return False


if __name__ == "__main__":
    s = Solution()
    matrix1 = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 16
    print(s.grid_search_matrix(matrix1, target))

    matrix2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    print(s.binary_search_matrix(matrix2, target))
    print(s.grid_search_matrix(matrix2, target))
