# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/8 21:19
@Author:     wz
@File:       有权重有放回背包问题.py
@Decs:
"""


"""
给定一个总数limit，现有[1,2,5,10,20,50,100]的币值大小的货币，不限个数，问有多少种方式凑出共limit

input: values: [1,2,5,10,20,50,100] limit: 5
output: 1/1/1/1/1 1/1/1/2 1/2/2 5 共四种
"""


class Solution:
    """"
     1、该题有 暴力递归 和 动态规划 两种解法。
    """

    def __init__(self, coins):
        self.coins = coins

    def combination(self, limit_price):
        print(self.recursion_combination(limit_price, 0))

    def recursion_combination(self, limit_price, index):
        """
        对硬币类型从左到右暴力穷举
        index 的含义为，当前递归过程讨论的时，对self.coins[index]这个币种
            for循环为取index位置，0次 1次 2次 至超出limit。
            1、base case: 当limit_price为0表示已经凑齐了，直接可以返回1；否则凑到最后超出所有的币种，limit_price都为凑满，则为0
            2、for循环展开：
                对index位置的币种取number次的情况，暴力递归
        """
        if limit_price == 0:
            return 1
        if index == len(self.coins):
            return 0

        ways = 0
        number = 0
        while number * self.coins[index] <= limit_price:
            ways += self.recursion_combination(limit_price - number * self.coins[index], index + 1)
            number += 1
        return ways

    def dp_combination(self, limit_price):
        """
        递归当中有两个变量，一个index 一个limit_price，所以dp应该是一个二维的表，dp[i][j]表示当剩余j的price需要凑的情况下，只使用下标为i及其之后的币种情况下，此时对i的讨论，一共有dp[i][j]种取法
        初始化为递归的base case，即：dp[...][0] = 1
                                    和 dp[len(self.coins)][...] = 0
        """

        index = len(self.coins)
        # 构建一个 (index + 1) * (limit_price + 1) 形状的dp表，分别表示 第index块的币种 和 剩余j的price
        dp = [[-1 for j in range(limit_price + 1)] for i in range(index + 1)]
        print(dp)

        # 初始化dp[len(self.coins)][...] = 0，即遍历完所有币种，还有待凑金额，凑失败了，返回0
        for i in range(len(dp[index])):
            dp[index][i] = 0

        # 初始化dp[...][0] = 1，即当待凑金额为0时，该位置为1；其实只初始化最后一列也可以
        dp[index][0] = 1
        # for i in range(len(dp)):
        #     dp[i][0] = 1

        for i in range(index - 1, -1, -1):  # 从base case 往前推
            for j in range(len(dp[i])):
                number = 0
                ways = 0  # 临时存储当前dp[i][j]值
                while number * self.coins[i] <= j:
                    ways += (dp[i + 1][j - number * self.coins[i]])
                    number += 1
                dp[i][j] = ways
        print(dp)

        return dp[0][limit_price]


if __name__ == "__main__":
    coins = [1, 2, 5, 10, 20, 50, 100]
    limit = 10
    s = Solution(coins)
    s.combination(limit)
    print(s.dp_combination(limit))
