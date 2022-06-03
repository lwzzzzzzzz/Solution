# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/26 0:30
@Author:     wz
@File:       QuickSort.py
@Decs:
"""

'''
快排: 平均时间复杂度O(NlogN) 最坏：O(N^2)
     不稳定
     空间复杂度 O(1)
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def quick_sort(self, left, right):

        if left >= right:
            return

        index = self.partition(left, right)
        self.quick_sort(left, index - 1)
        self.quick_sort(index + 1, right)

    def partition(self, left, right):
        p_l, ptr = left, left
        while ptr <= (right - 1):
            if self.nums[ptr] <= self.nums[right]:  # 条件'<' '<=' '>' '>=' 分别表示不同含义，顺序or逆序，是否考虑相等的情况
                self.nums[ptr], self.nums[p_l] = self.nums[p_l], self.nums[ptr]
                p_l += 1
            ptr += 1  # 本质上，不进入if，但是ptr自增过的索引，就是该算法最不优先考虑的区域，本题为大于区域，大于区域是在小于等于都排好了，自动好了。

        # 当用【考虑主排小于等于区域的两色问题】，假设pivot选择最后一个元素 求解时，最后只剩两个数的情况
        #   【ps: 插入位置为小于等于区域后一个，或者大于等于的第一个，即对应 p_l 或 p_r + 1】
        #     当最后[1,3]的情况，3为pivot时，p_l为1，无脑换p_l位置即可，自己换自己，结果为[1,3]；
        #     当最后[3,1]的情况，1为pivot时，p_l为0，无脑换p_l位置即可，结果为[1,3]；
        #     当为[1,4,3,2]，2为pivot时，循环结束时，p_l为1，无脑换没问题，结果为[1,2,4,3]；
        self.nums[right], self.nums[p_l] = self.nums[p_l], self.nums[right]
        print(self.nums)
        # ps:当有指针指示大于区域，即【三色问题】或【考虑主排大于等于区域的两色问题】时，假设pivot选择最后一个元素
        #     当最后[1,3]的情况无脑换存在问题，3为pivot时，p_r不动为0，此时无脑换位于大于区域的第一个数，即p_r+1即可，数组不越界（等于自己和自己换）
        #     当最后[3,1]的情况，1为pivot时，p_r为-1，无脑换p_r+1位置即可；
        #     当为[1,4,3,2]，2为pivot时，循环结束时，p_r为0，无脑换p_r+1即可，结果为[1,2,4,3]；
        # 为只剩两个数的情况不需要特殊处理，本质在于有pivot作为缓冲，准确指示交换位置的同时，不会导致数组越界。
        return p_l


if __name__ == "__main__":
    nums = [3, 1, 5, 3, 3]
    s = Solution(nums)
    left, right = 0, len(nums) - 1
    s.quick_sort(left, right)
    print(s.nums)
