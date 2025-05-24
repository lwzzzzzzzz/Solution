# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 21:42
@Author:     wz
@File:       杨辉三角.py
@Decs:
"""


class Solution:
    def function(self, numRows):
        res = []
        for i in range(numRows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j] + res[i - 1][j - 1])  # 当前值等于两肩之和
            res.append(row)
        return res


if __name__ == "__main__":
    s = Solution()
    triangle = s.function(5)
    for each in triangle:
        print(each)
