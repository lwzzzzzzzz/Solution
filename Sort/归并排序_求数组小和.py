# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/23 0:45
@Author:     wz
@File:       归并排序_求数组小和.py
@Decs:
"""

'''
给一个数组，求其小和

input：[3,1,5,4,3]  对于数组中5，小和为3+1=4；对于数组中2，小和为1=1
output：0+0+4+1+3=8
'''


class Solution:
    """
    一个数组最终小和 可以转化为： 1.左右两边分别求完小和，将小和相加 2.再将左右合并时产生的小和相加
        - 即当左右两边的数组分别有序时如：[3,1,5],[4,3]
        - 左小和：4 右小和：0；合并产生小和：4+1=5  --> 最终为4+0+5=9

    此问题可以转化为规模较小的、易解决的同一问题，且当子数组长度为1时，小和为0。立即推 --> 递归
    只不过当左右子数组都排好序的情况下，O(N)时间下就能求出合并所产生的小和；并且正好符合归并排序的框架，一切都是这么命中注定！
        - 当子数组有序[1,3,5],[3,4]，合并，对于右侧3产生小和1；对于右侧4产生1+3=4；最终为1+4=5
            - 我们换个思路，当有序时，对于左侧的1，产生小和1*len([3,4])=2；对于左侧的3，产生小和3*len([4])=3；对于左侧的5，产生小和5*len([])=0；最终为2+3+0=5
        * 正好在归并排序中我们可以做到上述转换
    """

    def __init__(self, nums):
        self.nums = nums
        self.res = 0

    def sum_small(self, left, right):

        if left >= right:
            return
        mid = (right - left) // 2 + left
        self.sum_small(left, mid)
        self.sum_small(mid + 1, right)
        self.merge(left, mid, right)

    def merge(self, left, mid, right):
        help = [0] * (right - left + 1)

        ptr = 0
        p_l, p_r = left, mid + 1
        while p_l <= mid and p_r <= right:
            # 当右侧严格大于左侧时，根据小和的定义才进行求和；此处牺牲了排序算法的稳定性，保障小和逻辑正确
            if self.nums[p_l] < self.nums[p_r]:
                help[ptr] = self.nums[p_l]
                self.res += (self.nums[p_l] * (right - p_r + 1))
                p_l += 1
            else:
                help[ptr] = self.nums[p_r]
                p_r += 1
            ptr += 1

        while p_l <= mid:
            help[ptr] = self.nums[p_l]
            p_l += 1
            ptr += 1

        while p_r <= right:
            help[ptr] = self.nums[p_r]
            p_r += 1
            ptr += 1

        for i in range(len(help)):
            self.nums[left + i] = help[i]


if __name__ == "__main__":
    nums = [3, 1, 5, 4, 3]
    s = Solution(nums)
    left, right = 0, len(nums) - 1
    s.sum_small(left, right)
    print(s.nums)
    print(s.res)
