# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/12 1:04
@Author:     wz
@File:       TwoSingleNumber.py
@Decs:
"""

'''
题目描述
给定一个非空数组，其中有两个数字出现一次，其他都出现两次，找出只出现一次的这两个数字。

输入输出样例
Input: nums = [2,2,1,3]
Output: 1,3

Input: nums = [4,1,2,1,2,6]
Output: 4,6

Input: nums = [1,2]
Output: 1,2
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def find_two_single_number(self):
        """
        此题同样利用xor运算
        1. 数组中存在两个出现一次的不同数字，则整个数组xor必然不为0，设为a
        2. 则选择a右起第一个不为0的位置的mask，对其进行and，根据结果将原本数组的分为两组，一组为0，一组非0，则两个数分别落在两组中
        3. 对两组数，分别组内xor得到结果
        """
        if len(self.nums) < 2:
            return False

        xor = 0
        for each in self.nums:
            xor ^= each

        res1, res2 = 0, 0
        mask = xor & (~xor + 1)
        for each in self.nums:
            if each & mask:
                res1 ^= each
            else:
                res2 ^= each

        return [res1, res2]


if __name__ == "__main__":
    nums = [2, 2, 1, -3]
    s = Solution(nums)
    print(s.find_two_single_number())
