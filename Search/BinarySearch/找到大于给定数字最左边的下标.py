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

    def find_leftmost_index(self, target):
        left = 0
        right = len(self.nums) - 1
        res = -1
        while left <= right:
            mid = (right - left) // 2 + left
            if target < self.nums[mid]:
                res = mid  # 因为本身进入该if分支的就是大于given的值，所以临时标记。当最后left==right的时候，mid就是第一个大于target的位置
                right = mid - 1
            elif target >= self.nums[mid]:  # 因为要找第一个大于target的值，所以相等时，应该吧搜索区间往大于target的位置移动
                left = mid + 1
        return res


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    s = Solution(nums)
    print(s.find_leftmost_index(7))
