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

            输入：网格中包含新鲜橘子(1)、腐烂橘子(2)、空格子(0)
            Step 1: 遍历整个网格，找出所有腐烂橘子作为初始队列
            Step 2: 如果全是新鲜橘子 → -1（无法腐烂）
            Step 3: 如果全是空格子 → 0
            Step 4: 进入 BFS：
                    a. 每一层代表一分钟
                    b. 将当前层所有腐烂橘子的邻居设为腐烂，并加入下一层队列
            Step 5: BFS 结束后检查是否还有新鲜橘子
            Step 6: 返回时间 d
        """
        m, n = len(grid), len(grid[0])
        all_zero = True  # 边界条件
        all_one = True  # 边界条件
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i, j])
                if grid[i][j] != 1:  # 边界条件
                    all_one = False
                if grid[i][j] != 0:  # 边界条件
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
        R, C = len(grid), len(grid[0])
        queue = collections.deque()

        # Step 1: 初始化队列，加入所有腐烂橘子
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (行, 列, 时间)

        # Step 2: 定义找邻居函数
        def find_neighbors(i, j):
            res = []
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < R and 0 <= nj < C:
                    res.append((ni, nj))
            return res

        # Step 3: 开始 BFS
        d = 0
        while queue:
            r, c, d = queue.popleft()
            for nr, nc in find_neighbors(r, c):
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    queue.append((nr, nc, d + 1))

        # Step 4: 检查是否还有新鲜橘子
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    return -1

        return d


if __name__ == "__main__":
    s = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(s.function(grid))
    print(grid)

    grid2 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(s.elegant_function(grid2))
    print(grid2)
