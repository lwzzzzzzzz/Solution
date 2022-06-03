# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/14 22:27
@Author:     wz
@File:       凑硬币问题.py
@Decs:
"""


class Solution:
    def __init__(self, coins):
        self.coins = coins

    def combination(self, limit_price):
        """
        现有硬币[2,5,2,6,3,7,...]若干枚，问凑得总数为10的方法有多少种？
         ps：该问题等价于权重都为1的背包问题
        """
        print("recursion_combination: ", self.recursion_combination(limit_price, 0))
        print("recursion_combination2: ", self.recursion_combination2(limit_price, 0, 0))

    def recursion_combination(self, sub_price, index):
        """
        easy
        1、base case有两种，当前剩余待凑额度为0，则返回1；一种是当前已经尝试完所有硬币，到达列表末尾，仍然不能满足，则返回0
        2、当前硬币该不该选择，则分情况讨论
        """

        if index == len(self.coins):
            if sub_price == 0:
                return 1
            else:
                return 0

        if sub_price >= self.coins[index]:  # 当前位置硬币 小于等于 待凑额度，则有两种选择
            return self.recursion_combination(sub_price - self.coins[index], index + 1) \
                   + self.recursion_combination(sub_price, index + 1)
        else:  # 否则只有不选这一种选择
            return self.recursion_combination(sub_price, index + 1)

    def dp_combination(self, limit_price):
        # dp[i][j]的含义为，当遍历到第i个硬币时，待凑金额还剩j时的组合数
        dp = [[0 for j in range(limit_price + 1)] for i in range(len(self.coins) + 1)]

        # 初始化
        for i in range(len(dp)):
            dp[i][0] = 1
        # for j in range(len(dp[0])):
        #     dp[len(self.coins)][j] = 0
        print(dp)

        for i in range(len(self.coins) - 1, -1, -1):
            for j in range(1, len(dp[i])):
                if j >= self.coins[i]:
                    dp[i][j] = dp[i + 1][j - self.coins[i]] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        print(dp)
        return dp[0][limit_price]

    def recursion_combination2(self, limit_price, accumulate_price, index):
        """
        easy
        1、base case有两种，当前剩余待凑额度为0，则返回1；一种是当前已经尝试完所有硬币，到达列表末尾，仍然不能满足，则返回0
        2、当前硬币该不该选择，则分情况讨论
        """

        if index == len(self.coins):
            if accumulate_price == limit_price:
                return 1
            else:
                return 0

        if limit_price - accumulate_price >= self.coins[index]:  # 当前位置硬币 小于等于 待凑额度，则有两种选择
            return self.recursion_combination2(limit_price, accumulate_price + self.coins[index], index + 1) \
                   + self.recursion_combination2(limit_price, accumulate_price, index + 1)
        else:  # 否则只有不选这一种选择
            return self.recursion_combination2(limit_price, accumulate_price, index + 1)

    def dp_combination2(self, limit_price):
        # dp[i][j]的含义为，当遍历到第i个硬币时（只使用下标为i及其之后的币种情况下），已凑金额为j时的组合数
        dp = [[0 for j in range(limit_price + 1)] for i in range(len(self.coins) + 1)]

        # 初始化
        # for i in range(len(dp)):
        #     dp[i][0] = 1
        for j in range(len(dp[0])):
            if j == limit_price:
                dp[len(self.coins)][j] = 1
            else:
                dp[len(self.coins)][j] = 0
        # for i in range(len(dp)):
        #     dp[i][0] = 1
        print(dp)

        for i in range(len(self.coins) - 1, -1, -1):
            for j in range(len(dp[i])):
                if limit_price - j >= self.coins[i]:
                    dp[i][j] = dp[i + 1][j + self.coins[i]] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        print(dp)
        return dp[0][0]

    def min_coins(self, limit_price):

        """
        现有硬币[2,5,2,6,3,7,...]若干枚，问凑得总数为10的方法，硬币最少需要多少枚？
         ps：该问题等价于权重都为1的背包问题变形
        """
        print(self.recursion_min_coins(limit_price, 0, 0))

    def recursion_min_coins(self, sub_price, index, cnt):
        """
        easy
        1、base case有两种，当前剩余待凑额度为0，则返回当前有多少枚硬币；一种是当前已经尝试完所有硬币，到达列表末尾，仍然不能满足，则返回初始值0
        2、当前硬币该不该选择，则分情况讨论
        """

        if index == len(self.coins):
            # 当遍历到最后时，待凑金额为0，则返回最后需要cnt块；待凑金额为不为，表示根本凑不出这些钱，返回-1
            if sub_price == 0:
                return cnt
            else:
                return -1

        if sub_price >= self.coins[index]:  # 当前位置硬币 小于等于 待凑额度，则有两种选择
            plus = self.recursion_min_coins(sub_price - self.coins[index], index + 1, cnt + 1)
            minus = self.recursion_min_coins(sub_price, index + 1, cnt)
            if minus == -1 and plus == -1:
                return -1
            else:
                if minus == -1:
                    return plus
                if plus == -1:
                    return minus
                return min(minus, plus)
        else:  # 否则只有不选这一种选择
            return self.recursion_min_coins(sub_price, index + 1, cnt)

    def min_coins2(self, limit_price):

        """
        现有硬币[2,5,2,6,3,7,...]若干枚，问凑得总数为10的方法，硬币最少需要多少枚？
         ps：该问题等价于权重都为1的背包问题变形
        """
        print("min coins recursion ways: ", self.recursion_min_coins2(limit_price, 0))

    def recursion_min_coins2(self, sub_price, index):
        """
        easy
        1、base case有两种，当前剩余待凑额度为0，则返回当前有多少枚硬币；一种是当前已经尝试完所有硬币，到达列表末尾，仍然不能满足，则返回初始值0
        2、当前硬币该不该选择，则分情况讨论
        """

        if index == len(self.coins):
            if sub_price != 0:
                return -1
            else:
                return 0

        if sub_price >= self.coins[index]:
            minus_this_coin = self.recursion_min_coins2(sub_price, index + 1)
            add_this_coin = self.recursion_min_coins2(sub_price - self.coins[index], index + 1)
            """
            对于包括和不包括当前这枚硬币的case，需要分类讨论，防止min(-1, 2)这种情况的出现
            1.选择和不选择当前硬币，都不能完成凑满任务，返回 -1
            2.不选择当前硬币，不能完成凑满任务；选择当前硬币，能完成凑满任务，返回 1 + add_this_coin
            3.不选择当前硬币，能完成凑满任务；选择当前硬币，不能完成凑满任务，返回 minus_this_coin
            4.选择和不选择当前硬币，都能完成凑满任务，返回 min(minus_this_coin, 1 + add_this_coin)
            """
            if minus_this_coin == -1 and add_this_coin == -1:
                return -1
            else:
                if minus_this_coin == -1:
                    return 1 + add_this_coin
                if add_this_coin == -1:
                    return minus_this_coin
                return min(minus_this_coin, 1 + add_this_coin)
        else:
            return self.recursion_min_coins2(sub_price, index + 1)

    def dp_min_coins(self, limit_price):
        """
        easy
        1、base case有两种，当前剩余待凑额度为0，则返回当前有多少枚硬币；一种是当前已经尝试完所有硬币，到达列表末尾，仍然不能满足，则返回初始值0
        2、当前硬币该不该选择，则分情况讨论
        """

        # dp[i][j]含义为只是用下标i或之后的硬币，凑齐j块钱最少需要多少块硬币
        dp = [[-1 for j in range(limit_price + 1)] for i in range(len(self.coins) + 1)]

        # 初始化
        for j in range(len(dp[0])):
            if j == 0:
                dp[len(self.coins)][j] = 0
            else:
                dp[len(self.coins)][j] = -1

        for i in range(len(self.coins) - 1, -1, -1):
            for j in range(len(dp[i])):
                if j >= self.coins[i]:
                    minus_this_coin = dp[i + 1][j]
                    add_this_coin = dp[i + 1][j - self.coins[i]]
                    if minus_this_coin == -1 and add_this_coin == -1:
                        dp[i][j] = -1
                    elif minus_this_coin == -1 or add_this_coin == -1:
                        if minus_this_coin == -1:
                            dp[i][j] = 1 + add_this_coin
                        if add_this_coin == -1:
                            dp[i][j] = minus_this_coin
                    else:
                        dp[i][j] = min(minus_this_coin, 1 + add_this_coin)
                else:
                    dp[i][j] = dp[i + 1][j]

        print(dp)
        return dp[0][limit_price]


if __name__ == "__main__":
    coins = [1, 3, 3, 1, 1, 2]
    limit = 7
    # for i in range(4 - 1, -1, -1):
    #     print(i)
    s = Solution(coins)
    s.combination(limit)
    print("dp ways: ", s.dp_combination(limit))
    print("dp2 ways: ", s.dp_combination2(limit))

    s.min_coins(limit)
    s.min_coins2(limit)
    print("min coins dp ways: ", s.dp_min_coins(limit))
