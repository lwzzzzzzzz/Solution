# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 1:02
@Author:     wz
@File:       搜索二维数组.py
@Decs:
"""


"""
每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
输入：matrix = 
[[1, 4, 7, 11, 15]
,[2, 5, 8, 12, 19]
,[3, 6, 9, 16, 22]
,[10,13,14,17, 24]
,[18,21,23,26,30]]
target = 5
输出：true

思路：从最后一列去考虑，如果比最后一个元素大，那么他肯定位于下一列，当遍历到最后一列某个元素大于target，这时候顺序从后往前遍历找到target
O(M+N)时间复杂度

ps:这种题目一般可以，一边递增 一边递减 遍历，时间复杂度显著下降
"""

class Solution:
    def function(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while row < m - 1 and col >= 0:
            if matrix[row][col] > target:
                col -= 1
            elif matrix[row][col] < target:
                row += 1
            else:
                return [row, col]
        return False



if __name__ == "__main__":
    s = Solution()
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    print(s.function(matrix, target))