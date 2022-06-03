# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/30 23:15
@Author:     wz
@File:       打印某字符串的所有子序列.py
@Decs:
"""

'''
打印某字符串的包含空字符串的所有子序列
eg:
input: abc
output: abc ab ac bc a b c None
'''


class Solution:
    """
    一道典型的满二叉树递归题目，返回最后所有叶子节点的值，只需要每次传递给左右节点的当前子串是否需要当前字符，即a，再往下是ab，还是仍然是a。
    """
    def __init__(self, s):
        self.s = s

    def both_sub_string(self):
        s_list = list(self.s)
        res = []
        self.sub_string(0, "", res, s_list)
        return res

    def sub_string(self, depth, cur_str, res, s_list):
        if depth == len(self.s):
            res.append(cur_str)
            return

        need_cur_str = cur_str + s_list[depth]
        self.sub_string(depth + 1, need_cur_str, res, s_list)
        abandon_cur_str = cur_str
        self.sub_string(depth + 1, abandon_cur_str, res, s_list)


if __name__ == "__main__":
    s = "abc"

    so = Solution(s)
    print(so.both_sub_string())
