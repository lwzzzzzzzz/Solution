# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 1:04
@Author:     wz
@File:       盛最多水的容器.py
@Decs:
"""


class Solution:
    def function(self, nums: list[int]):
        left, right = 0, len(nums) - 1
        res = 0
        while left < right:
            area = (right - left) * min(nums[right], nums[left])
            # 因为左右指针要向中间移动，底要变小，要让面积最大，只能移动高更小的那根指针，直到跳出循环
            if nums[right] <= nums[left]:
                right = right - 1
            else:
                left = left + 1
            res = max(res, area)
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function([0, 1, 3, 2, 12])
    print(xxx)
