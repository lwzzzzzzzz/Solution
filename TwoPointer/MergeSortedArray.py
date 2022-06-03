# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/8 1:15 上午
@Author:     wz
@File:       MergeSortedArray.py
@Decs:
"""

'''
question:
给你两个有序整数数组nums1 和 nums2，请你将 nums2 合并到nums1中，使 nums1 成为一个有序数组。
初始化nums1 和 nums2 的元素数量分别为m 和 n 。你可以假设nums1 的空间大小等于m + n，这样它就有足够的空间保存来自 nums2 的元素。

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]

'''


class Solution:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2

    def merge(self, m, n):

        # 题目很简单，双指针一次遍历过去就行，直到其中一个数组越界
        # 主要是有一个可以优化的点，就是减少元素的移动，可以从后往前遍历（类似与插入排序移动元素）每次迭代只移动一个，避免每次移动一串
        length = m + n
        while m > 0 and n > 0:
            if self.nums1[m - 1] > self.nums2[n - 1]:
                self.nums1[m + n - 1] = self.nums1[m - 1]
                m -= 1
            else:
                self.nums1[m + n - 1] = self.nums2[n - 1]
                n -= 1

        print(m, n)

        # 只有当nums2存在多余的情况需要将nums2里的所有元素放入nums1；因为最终返回nums1，故nums1内存在多余元素可不用考虑。
        if n > 0:
            self.nums1[0: m + n] = self.nums2[0: n]

        return self.nums1[0: length]


if __name__ == "__main__":
    nums1 = [0, 0, 0, 0, 0, 0, 1, 3, 5]
    m = 3
    nums2 = [0, 0, 0, 6, 8]
    n = 5

    solution = Solution(nums1, nums2)
    print(solution.merge(m, n))
