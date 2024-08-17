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
    # res = -1
    while left <= right:  # key: 二分的right和left终止条件有等于
        mid = (right - left) // 2 + left  # 同时，mid位置就是被查找到的位置，根据需要的边界确定res=mid应该加在哪个if的分支
        if nums[mid] < t:
            left = mid + 1
            # res = mid  # 表示找到小于t的最大值，因为nums[mid] < t
        elif nums[mid] > t:
            right = mid - 1
            # res = mid  # 表示找到大于t的最小值，因为nums[mid] > t
        else:
            # res = mid  # 表示找到等于t的位置
            return mid
    return False


if __name__ == "__main__":
    nums = [1, 4, 7, 1, 3, 7, 9, 2, 0, 3]
    nums.sort()
    print(nums)
    print(binary_search(nums, 4))
    # print(nums)
