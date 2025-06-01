# _*_ coding: utf-8 _*_
"""
@Date:       2021/4/29 11:05 上午
@Author:     wz
@File:       InsertSort.py
@Decs:
"""


class InsertSort():
    """
    naive sort algorithm
    时间复杂度：best:O(N)  worst:O(N^2) mean:O(N^2)
    空间复杂度：O(1)
    属性：稳定
    """

    def __init__(self, nums):
        self.nums = nums

    def insert_sort(self):
        # 每次取下标为i的元素，将其插入到之前已经有序的序列中
        for i in range(len(self.nums)):
            now = self.nums[i]
            j = i - 1
            while j >= 0 and self.nums[j] > now:  # 找到插入位置
                self.nums[j + 1] = self.nums[j]
                j -= 1

            self.nums[j + 1] = now  # 插入到小于now的元素的最右边

        return self.nums


if __name__ == "__main__":
    nums = [1, 4, 6, 7, 2, 4, 6, 7, 9, 100]
    sort = InsertSort(nums)
    print(sort.insert_sort())
