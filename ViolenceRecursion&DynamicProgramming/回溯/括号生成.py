# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 22:54
@Author:     wz
@File:       括号生成.py
@Decs:
"""

"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
"""

class Solution:
    """
        回溯
        只要左括号和右括号都达到要求返回。当左括号不足n个时，进行回溯；
                                    当左括号大于右括号时，可以添加右括号，进行回溯
        这里没有用for的原因在于，回溯的可能性只有两个，加左括号 or 加右括号，已经用if做了遍历，就没有for什么事了。
    """
    def function(self, n):
        res = []

        def combine(path, left_k, right_k):
            if left_k == n and right_k == n:
                res.append(''.join(path))
                return

            if left_k < n:
                path.append('(')
                combine(path, left_k + 1, right_k)
                path.pop()

            if right_k < left_k:
                path.append(')')
                combine(path, left_k, right_k + 1)
                path.pop()

        combine([], 0, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.function(4))
