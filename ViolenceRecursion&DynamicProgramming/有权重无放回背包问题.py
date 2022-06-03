# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/3 1:21
@Author:     wz
@File:       有权重无放回背包问题.py
@Decs:
"""

"""
假设有一组货物，重量为weights数组，这组货物的价值为values数组，现给定一个重量limit，要求在这个限制下，拿到价值最高的货物组合。

input: weights: [2,4,3,1] values: [1,2,3,4] limit: 5
output: 总重量为3+1=4，价值最大为3+4=7
"""


class Solution:
    """"
     1、该题有 暴力递归 和 动态规划 两种解法。
    """

    def __init__(self, weights, values):
        self.w = weights
        self.v = values

    def max_value(self, limit_w):
        print(self.recursion_max_value(limit_w, 0, 0))

    def recursion_max_value(self, limit_w, already_w, index):
        """
        从左往右依次遍历，取index位置或者不取index位置。
            1、base case: 当取到顶时，即没有货物了，则返回0
            2、两种情况：
                2.1 当压根不能取的情况（直接超重），跳过index位置；
                2.2 当可以取的时候，求取和不取两种情况的最大值，保证value最大
        """
        if index == len(self.v):
            return 0

        if self.w[index] + already_w > limit_w:
            return self.recursion_max_value(limit_w, already_w, index + 1)
        else:
            return max(self.recursion_max_value(limit_w, already_w, index + 1),
                       self.v[index] + self.recursion_max_value(limit_w, self.w[index] + already_w, index + 1))


if __name__ == "__main__":
    weights = [1, 3, 3, 1]
    values = [1, 4, 3, 4]
    limit = 5
    s = Solution(weights, values)
    s.max_value(limit)
