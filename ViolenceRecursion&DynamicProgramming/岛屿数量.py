# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/28 23:58
@Author:     wz
@File:       岛屿数量.py
@Decs:
"""


class Solution:
    """
        思路是用遍历算法，每次都把所有相邻的“1”遍历出来，并置为“0”，当为一个连通区域的就都变成“0”，
        遍历整个矩阵的“1”，在遍历矩阵的循环中，调用了几次遍历函数，也就有多少个连通区域，即岛屿数
        1. dfs
        2. bfs

        ps：该题给出了矩阵岛屿问题的结题模版
    """

    def function(self, grid):
        n, m = len(grid), len(grid[0])

        def dfs(grid, i, j):
            if i < 0 or i > n - 1 or j < 0 or j > m - 1:  # 如果超出grid边界，return
                return

            if grid[i][j] == "0" or grid[i][j] == "2":  # 如果不是"1"，或者被访问过，return
                return

            grid[i][j] = "2"  # 标记为被访问
            dfs(grid, i-1, j)  # 往上
            dfs(grid, i+1, j)  # 往下
            dfs(grid, i, j-1)  # 往左
            dfs(grid, i, j+1)  # 往右

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(grid, i, j)  # 每一个连通分量进入一次dfs函数
                    res += 1
        return res


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    print(s.function(grid))
