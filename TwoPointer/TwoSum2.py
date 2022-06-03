# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/7 1:21 下午
@Author:     wz
@File:       TwoSum2.py
@Decs:
"""

'''

question:
在一个增序的整数数组里找到两个数，使它们的和为给定值。已知有且只有一对解。

Examples:
输入是一个数组（numbers）和一个给定值（target）。输出是两个数的位置，从1 开始计数。
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]

'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def two_sum(self, target):

        nums = sorted(self.nums)
        print(nums)

        res = []
        # 对撞指针遍历排好序的list，两数和大于target -> 移动右指针；两数和小于target -> 移动左指针；相等 -> 返回
        i, j = 0, len(nums) - 1
        while j > i:
            if nums[j] + nums[i] > target:
                j -= 1
            elif nums[j] + nums[i] < target:
                i += 1
            else:
                res = [i, j]
                break
        return res


if __name__ == "__main__":
    nums = [1, 6, 6, 2, 1, 9, 7, 5, 100]
    target = 9

    solution = Solution(nums)
    print(solution.two_sum(target))
