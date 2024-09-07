# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 20:59
@Author:     wz
@File:       分割等和子集.py
@Decs:
"""

"""
判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
输入：nums = [1,5,5,6,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [5,6] 。
"""
class Solution:
    def function(self, nums):
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2:  # 不能被2整除，直接false
            return False

        target = total // 2  # 背包容量
        n = len(nums)  # 物品个数
        dp = [[False] * (target + 1) for _ in range(n + 1)]  # 状态：dp[m][n]由前m个物品是否能填满容量为n的背包
        # base case 当背包容量为0时，可以填满背包
        dp[0][0] = True

        for i in range(0, n):
            for c in range(target + 1):
                if c < nums[i]:  # 如果背包装不下第j个物品
                    dp[i + 1][c] = dp[i][c]
                else:
                    dp[i + 1][c] = dp[i][c] or dp[i][c - nums[i]]

        print(dp)
        return dp[n][target]

    def function2(self, nums):
        if len(nums) < 2:
            return False
        total = sum(nums)
        if total % 2:  # 不能被2整除，直接false
            return False

        target = total // 2  # 背包容量
        n = len(nums)  # 物品个数
        dp = [0] * (target + 1)  # 状态：dp[i]是否能填满容量为n的背包
        # base case 当背包容量为0时，可以填满背包
        dp[0] = 1

        for i in range(0, n):
            for c in range(target, -1, -1):
                if c >= nums[i]:  # 背包容量能够装下第i个物品
                    dp[c] = dp[c] + dp[c - nums[i]]  # 当取dp[c] + dp[c - nums[i]]就是满足和为target的方案数

        print(dp)
        return dp[target] > 1


if __name__ == "__main__":
    s = Solution()
    nums = [1,2,3,3,3]
    print(s.function(nums))
    print(s.function2(nums))