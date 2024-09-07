# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 20:08
@Author:     wz
@File:       连续子序列最大乘积.py
@Decs:
"""
import sys

"""
输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
"""

class Solution:
    """
        和连续子序列最大和一样的思路，本题中dp[i]表示遍历到i位置的最大值。
        不过对于乘积来说，有正负号的讨论，这时候就需要同时记录最小值，每次看看是不是由最小值负负得正的最大值
    """
    def function2(self, nums):
        dp = [-sys.maxsize] * len(nums)
        min_value, max_value = [0] * len(nums), [0] * len(nums)
        dp[0], min_value[0], max_value[0] = nums[0], nums[0], nums[0]
        for i in range(1, len(nums)):
            a = min_value[i - 1] * nums[i]
            b = max_value[i - 1] * nums[i]
            max_value[i] = max(a, b, nums[i])  # 比较a, b, nums[i]三种情况，最大值只能在这三个里面选
            min_value[i] = min(a, b, nums[i])  # 同理
            dp[i] = max(dp[i-1], max_value[i])  # 取不取当前元素
        return dp[len(nums)-1]

    def function(self, nums):
        res = nums[0]
        min_value, max_value = nums[0], nums[0]
        for i in range(1, len(nums)):
            a = min_value * nums[i]
            b = max_value * nums[i]
            min_value = min(min(a, b), nums[i])
            max_value = max(max(a, b), nums[i])
            res = max(max_value, res)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, -2, -2, -2, 4]
    print(s.function(nums))
    print(s.function2(nums))
