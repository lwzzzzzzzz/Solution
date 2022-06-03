# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/18 1:00
@Author:     wz
@File:       MergeSort2.py
@Decs:
"""


def sort1(arr, left, right):
    if left == right:
        return

    mid = (right - left) // 2 + left
    sort1(arr, left, mid)  # 先排左侧
    sort1(arr, mid + 1, right)  # 再排右侧
    merge(arr, left, mid, right)  # 合并左右


def merge(arr, left, mid, right):
    #  构建辅助空间
    help1 = [0] * len(arr)  # 这里可以不用len(arr)这么长，因为可以初始化ptr=0，43行arr的下标写成index=left+i

    #  将left-mid-right区间合并成有序
    ptr, l, r = left, left, mid + 1
    while l <= mid and r <= right:
        if arr[l] <= arr[r]:
            help1[ptr] = arr[l]
            l += 1
        else:
            help1[ptr] = arr[r]
            r += 1
        ptr += 1
    while l <= mid:  # 右侧先结束，左侧填入即可
        help1[ptr] = arr[l]
        ptr += 1
        l += 1
    while r <= right:  # 左侧先结束，右侧填入即可
        help1[ptr] = arr[r]
        ptr += 1
        r += 1

    #  将辅助空间内已排好序的部分搬到原空间
    for index in range(left, right + 1):
        arr[index] = help1[index]


arr = [3, 1, 6, 8, 2, 7]
sort1(arr, 0, len(arr) - 1)
print(arr)
