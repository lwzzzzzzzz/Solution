# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/28 22:53
@Author:     wz
@File:       求连续子序列最大和.py
@Decs:
"""

"""
给定一列表，求其连续子序列中，和最大的值
eg：[-1, 3, -2, 5, -2, 3, 4] 最大字串为[3, -2, 5, -2, 3, 4]，最大和为11
"""


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def sub_list_max_sum(self):
        """
        递归的含义是：以当前下标为结束的子串的最大和，则入参应该为len(self.nums) - 1
        """
        res = self.recursion_sub_list_max_sum(len(self.nums) - 1)
        print("recursion subList max sum:", res)

    def recursion_sub_list_max_sum(self, index):
        # 子串为空返回0
        if index == 0:
            return 0
        # 讨论当前元素，为正数直接加进来；为负数讨论前面的结果和当前和是否为正数
        if self.nums[index] < 0:
            return max(self.recursion_sub_list_max_sum(index - 1) + self.nums[index], 0)
        else:
            return self.recursion_sub_list_max_sum(index - 1) + self.nums[index]

    def dp_sub_list_max_sum(self):
        # 初始化dp数组
        dp = [0 for i in range(len(self.nums))]
        dp[0] = 0

        for i in range(1, len(self.nums)):
            # 讨论当前元素，为正数直接加进来；为负数讨论前面的结果和当前和是否为正数
            if self.nums[i] < 0:
                dp[i] = max(dp[i - 1] + self.nums[i], 0)
            else:
                dp[i] = dp[i - 1] + self.nums[i]
        print("dp subList max sum:", dp[len(self.nums) - 1])
        return dp[len(self.nums) - 1]


if __name__ == "__main__":
    nums = [-1, 3, -2, 5, -2, 3, 4]

    s = Solution(nums)
    s.sub_list_max_sum()
    s.dp_sub_list_max_sum()
