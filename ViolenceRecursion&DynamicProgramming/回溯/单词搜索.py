# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 23:57
@Author:     wz
@File:       单词搜索.py
@Decs:
"""

"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = 
[["A","B","C","E"]
,["S","F","C","S"]
,["A","D","E","E"]], 
word = "ABCCED"
输出：true

"""


class Solution:
    """
        该题和岛屿问题是相似的，都是对矩阵做dfs的搜索，不过这题的回溯需要恢复现场，而岛屿问题不需要恢复现场
    """
    def exist(self, board, word):
        if not word:
            return False

        n = len(board)
        m = len(board[0])

        def dfs(board, word, index, row, col):
            if index == len(word):
                return True

            if row < 0 or col < 0 or row >= n or col >= m:  # 如果超出board边界，说明遍历到这个位置还不满足题意 return false
                return False

            if board[row][col] != word[index]:  # 如果当前元素不满足题意，return false
                return False

            board_val = board[row][col]
            board[row][col] = '0'  # 处理该节点
            # 该过程表示，只要后续有一个方向满足题意，则当前位置可以取，可以继续往下递归，return true 所以全部用or连接
            result = dfs(board, word, index + 1, row - 1, col) \
                     or dfs(board, word, index + 1, row + 1, col) \
                     or dfs(board, word, index + 1, row, col - 1) \
                     or dfs(board, word, index + 1, row, col + 1)
            board[row][col] = board_val  # 恢复现场

            return result

        for i in range(n):
            for j in range(m):
                if word[0] == board[i][j] and dfs(board, word, 0, i, j):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(s.exist(board, word))