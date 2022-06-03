# _*_ coding: utf-8 _*_
"""
@Date:       2022/1/16 21:09
@Author:     wz
@File:       无序不相等数组找局部最小值.py
@Decs:
"""

'''
给定一无序且两两之间为不相等数字的list，找到其中一个局部最小的位置

input：[5,7,7,8,8,10]  
output：0
注：因为5,7的顺序，5为局部最小值，数组中不止一处，输出一处即可

input：[3,2,7,6,5,4]  
output：1
注：因为3,2,7的顺序，2为局部最小值；同时5,4的顺序，4也是局部最小值
'''


class Solution:
    def __init__(self, nums):
        self.nums = nums

    def find_anyone_local_minimum(self):

        if self.nums[0] < self.nums[1]:
            return 0

        i = len(self.nums) - 1
        if self.nums[i] < self.nums[i - 1]:
            return i

        left = 0
        right = len(self.nums)
        while left <= right:
            mid = (right - left) // 2 + left
            if self.nums[mid - 1] > self.nums[mid] and self.nums[mid] < self.nums[mid + 1]:
                return mid
            elif self.nums[mid - 1] <= self.nums[mid]:
                right = mid - 1
            elif self.nums[mid] >= self.nums[mid + 1]:
                left = mid + 1


if __name__ == "__main__":
    nums = [7, 6, 12, 11, 8, 10]
    s = Solution(nums)
    print(s.find_anyone_local_minimum())


