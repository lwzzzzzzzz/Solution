# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/13 1:49
@Author:     wz
@File:       Demo.py
@Decs:
"""

'''
二分查找demo
'''


def binary_search(nums, t):
    left, right = 0, len(nums) - 1
    while left <= right:  # key: 二分的right和left终止条件有等于
        mid = (right - left) // 2 + left
        if nums[mid] < t:
            left = mid + 1
        elif nums[mid] > t:
            right = mid - 1
        else:
            return mid
    return False


if __name__ == "__main__":
    nums = [1, 4, 7, 1, 3, 7, 9, 2, 0, 3]
    nums.sort()
    print(nums)
    print(binary_search(nums, 4))
    # print(nums)
