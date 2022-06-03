# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/12 0:51
@Author:     wz
@File:       SingleNumber.py
@Decs:
"""

'''
题目描述
给定一个非空数组，其中只有一个数字出现一次，其他都出现两次，找出只出现一次的数字。

输入输出样例
Input: nums = [2,2,1]
Output: 1

Input: nums = [4,1,2,1,2]
Output: 4

Input: nums = [1]
Output: 1
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def find_single_number(self):
        """
        此题利用 a^a=0 0^a=a
        """
        if not self.nums:
            return False
        res = 0
        for each in self.nums:
            res ^= each
        return res


if __name__ == "__main__":
    nums = [2, 2, 1]
    s = Solution(nums)
    print(s.find_single_number())
