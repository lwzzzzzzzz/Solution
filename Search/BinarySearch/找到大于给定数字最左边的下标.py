# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/16 20:01
@Author:     wz
@File:       找到大于给定数字最左边的下标.py
@Decs:
"""

'''
给定一有序list，找到大于给定数字最左边的下标

input：[5,7,7,8,8,10]  6
output：1
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def find_leftmost_index(self, given):
        left = 0
        right = len(self.nums) - 1
        res = -1
        while left <= right:
            mid = (right - left) // 2 + left
            if given < self.nums[mid]:
                res = mid
                right = mid - 1
            elif given >= self.nums[mid]:
                left = mid + 1
                # if mid <= given:
                #     res = mid
        return res


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    s = Solution(nums)
    print(s.find_leftmost_index(5))
