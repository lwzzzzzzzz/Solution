# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 14:57
@Author:     wz
@File:       腐烂的橘子.py
@Decs:
"""
import collections


class Solution:
    def function(self, grid):
        """
            用一般的bfs方式实现，可以作为矩阵的bfs模板使用
        """
        m, n = len(grid), len(grid[0])
        all_zero = True
        all_one = True
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] != 1:
                    all_one = False
                if grid[i][j] != 0:
                    all_zero = False
        if all_one:  # 边界条件
            return -1
        if all_zero:  # 边界条件
            return 0

        def find_neighbors(i, j):
            tmp = []
            if 0 <= i + 1 < m:
                tmp.append([i + 1, j])
            if 0 <= i - 1 < m:
                tmp.append([i - 1, j])
            if 0 <= j + 1 < n:
                tmp.append([i, j + 1])
            if 0 <= j - 1 < n:
                tmp.append([i, j - 1])
            return tmp

        d = -1
        while queue:
            d += 1
            for k in range(len(queue)):  # 通过队列实现广度优先搜索，和树的层序遍历一样
                i, j = queue.pop(0)
                neighbor = find_neighbors(i, j)  # 找到下一层的元素
                for ni, nj in neighbor:
                    if grid[ni][nj] == 1:  # 当可以被腐烂时进入bfs
                        grid[ni][nj] = 2
                        queue.append([ni, nj])
            # print(queue, d)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return d


    def elegant_function(self, grid):
        """
            把状态带入到queue中，简化了边界条件的处理
        """
        R, C = len(grid), len(grid[0])

        # queue - all starting cells with rotting oranges
        queue = collections.deque()
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c, 0))

        def find_neighbors(i, j):
            tmp = []
            if 0 <= i + 1 < R:
                tmp.append([i + 1, j])
            if 0 <= i - 1 < R:
                tmp.append([i - 1, j])
            if 0 <= j + 1 < C:
                tmp.append([i, j + 1])
            if 0 <= j - 1 < C:
                tmp.append([i, j - 1])
            return tmp

        d = 0
        while queue:
            r, c, d = queue.popleft()
        neighbor = find_neighbors(r, c)  # 找到下一层的元素
        for nr, nc in neighbor:
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        if any(1 in row for row in grid):
            return -1
        return d


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(s.function(grid))
    print(grid)
