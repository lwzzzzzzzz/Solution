# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 21:44
@Author:     wz
@File:       只出现一次的数字.py
@Decs:
"""


class Solution:
    def function(self, nums):
        res = 0
        for i in range(len(nums)):
            res ^= nums[i]  # 利用0^x=x x^x=0的性质
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    print(s.function(nums))
