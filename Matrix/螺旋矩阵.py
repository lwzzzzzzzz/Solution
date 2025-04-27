# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 15:39
@Author:     wz
@File:       螺旋矩阵.py
@Decs:
"""

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1

        while True:
            for i in range(left, right + 1):  # 遍历上边界
                res.append(matrix[up][i])
            up += 1  # 遍历完后上边界+1
            if down < up:  # 检查是否越界，越界则break
                break

            for i in range(up, down + 1):  # 遍历右边界
                res.append(matrix[i][right])
            right -= 1  # 遍历完后右边界-1
            if right < left:
                break

            for i in range(right, left - 1, -1):  # 遍历下边界
                res.append(matrix[down][i])
            down -= 1  # 遍历完后下边界-1
            if down < up:
                break

            for i in range(down, up - 1, -1):  # 遍历左边界
                res.append(matrix[i][left])
            left += 1  # 遍历完后左边界+1
            if right < left:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    # [1, 1, 1],
    # [1, 0, 1],
    # [1, 1, 1]
    print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    # [1, 2, 3, 4],
    # [5, 6, 7, 8],
    # [9, 10, 11, 12]
    print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
