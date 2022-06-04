# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/5 0:08
@Author:     wz
@File:       将0移动到最后.py
@Decs:
"""


class Solution:
    """
        一道典型的双指针题，左指针指示插入位置，右指针遍历所有元素 （本质是荷兰国旗问题）
    """
    def moveZeroes(self, nums):
        not_zero, i = 0, 0  # not_zero记录非0元素插入的位置
        while i < len(nums):
            if nums[i] != 0:
                nums[not_zero], nums[i] = nums[i], nums[not_zero]
                not_zero += 1  # 插入完成，not_zero ++
            i += 1
        return nums[:not_zero]


if __name__ == "__main__":
    s = Solution()
    nums = [0, 1, 0, 3, 12]
    print("res：", s.moveZeroes(nums))
