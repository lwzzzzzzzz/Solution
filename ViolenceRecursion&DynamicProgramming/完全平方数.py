# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/30 0:10
@Author:     wz
@File:       完全平方数.py
@Decs:
"""
import sys


class Solution:
    """
    给你一个整数n，返回和为n的完全平方数的最少数量。
    输入：n = 12
    输出：3
    解释：12 = 4 + 4 + 4
    """
    def function(self, n):
        dp = [sys.maxsize] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # dp[i]表示最少为几个数的平方和。dp状态转移方程表示，12=1+11；12=4+8；12=9+3取其中最小的
                dp[i] = min(dp[i], dp[i-j*j] + 1)
                j += 1
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.function(1))
