# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/4 0:15
@Author:     wz
@File:       最长递增子序列.py
@Decs:
"""


class Solution:
    """
        dp[i]的意义表示，当nums[i]被选择后，以该位置为终点的序列，最长递增子序列为多长。
        1. dp[0]第一个元素，显然应该是dp[0]=1
        2. dp[i]时，我们应该遍历在nums[i]之前的更小的元素，选择其最大的，然后 +1 (把nums[i]选上)
        3. 最后返回 max(dp)
    """
    def function(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            for j in range(i):  # 遍历i前面元素
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])  # 取前面元素最大的
            dp[i] += 1
        print(dp)
        return max(dp)

if __name__ == "__main__":
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.function(nums))
