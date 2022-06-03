# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/13 0:15
@Author:     wz
@File:       机器人从s到e问题.py
@Decs:
"""


"""
假设一排有N个格子，一个机器人位于S（S在1-N个格子内），要走到E（E也在1-N个格子内）位置，必须走k步，问有多少种走法。
"""


class Solution:
    def __init__(self, n, s, e, k):
        self.n = n
        self.s = s
        self.e = e
        self.k = k

    def s2e(self):
        """
        显然n，e两个值是固定的，尝试方法则可以是，从左往右试，当开始位置分别是1-n的情况
        """
        print("ways: ", self.recursion_s2e(self.s, self.e, self.k))

    def recursion_s2e(self, s, e, k):
        if s == e and k == 0:  # 当步数用完且s==e了，显然为一种方法
            return 1
        if s != e and k == 0:  # 当步数用完且s!=e了，显然不是一种方法
            return 0

        if s == 1:  # 当走到最左侧，只有往右一种走法
            return self.recursion_s2e(s + 1, e, k - 1)
        if s == self.n:  # 当走到最右侧，只有往左一种走法
            return self.recursion_s2e(s - 1, e, k - 1)

        return self.recursion_s2e(s + 1, e, k - 1) + self.recursion_s2e(s - 1, e, k - 1)

    def dp_s2e(self):
        # 其中j表示起点位置，i表示还剩多少步
        dp = [[-1 for j in range(self.n)] for i in range(self.k + 1)]

        for j in range(len(dp[0])):
            if j == self.e-1:
                dp[0][j] = 1
            else:
                dp[0][j] = 0

        for i in range(1, len(dp)):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j+1]
                elif j == self.n-1:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        print(dp)

        # 这里千万不要返回dp[self.k][self.e-1]，整个dp和e位置其实没有关系，
        # 要牢记dp的定义，这里的dp[i][j]表达式定义为给定跑i步，j位置为起点的情况下，方法有多少次，显然应该是dp[self.k][self.s-1] 
        return dp[self.k][self.s-1]



if __name__ == "__main__":

    s1 = Solution(4, 1, 3, 4)
    s1.s2e()
    print("dp ways: ", s1.dp_s2e())
