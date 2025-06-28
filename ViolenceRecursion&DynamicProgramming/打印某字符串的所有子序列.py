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

    def both_sub_string(self, s):
        result = []

        def dfs(index, current):
            if index == len(s):
                result.append(current)
                return
            # 不选当前字符
            dfs(index + 1, current)
            # 选当前字符
            dfs(index + 1, current + s[index])

        dfs(0, "")
        return result


if __name__ == "__main__":
    s = "abc"

    so = Solution()
    print(so.both_sub_string(s))
