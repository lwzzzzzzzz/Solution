# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/23 17:49
@Author:     wz
@File:       打印所有逆序对.py
@Decs:
"""

'''
给定一个数组，打印其中所有逆序对。

input：[3,1,5,4,3]  
output：(3,1) (5,4) (5,3) (4,3)
'''


class Solution:
    """
    此题同理于【求数组小和】
    该问题也是可以分解为规模较小的、易解决的左右子问题，且当子数组长度为1时，没有逆序对直接返回。立即推 --> 递归
    也是当左右子数组为有序时，时间复杂度O(N) --> 归并排序
    """
    def __init__(self, nums):
        self.nums = nums
        self.res = []

    def find_reverse_pair(self, left, right):

        if left >= right:
            return
        mid = (right - left) // 2 + left
        self.find_reverse_pair(left, mid)
        self.find_reverse_pair(mid + 1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):

        _help = [0] * (right - left + 1)
        p_l, p_r = left, mid + 1
        ptr = 0

        while p_l <= mid and p_r <= right:
            if self.nums[p_l] > self.nums[p_r]:  # 求逆序对，则只有右边小于左边才记录下来，且记录到辅助数组；排序保持稳定性
                self.res.append([self.nums[p_l], self.nums[p_r]])
                _help[ptr] = self.nums[p_r]
                p_r += 1
            else:
                _help[ptr] = self.nums[p_l]
                p_l += 1
            ptr += 1

        while p_l <= mid:
            _help[ptr] = self.nums[p_l]
            p_l += 1
            ptr += 1

        while p_r <= right:
            _help[ptr] = self.nums[p_r]
            p_r += 1
            ptr += 1

        for i in range(len(_help)):
            self.nums[left + i] = _help[i]


if __name__ == "__main__":
    nums = [3, 1, 5, 4, 3]
    s = Solution(nums)
    left, right = 0, len(nums) - 1
    s.find_reverse_pair(left, right)
    print(s.nums)
    print(s.res)
