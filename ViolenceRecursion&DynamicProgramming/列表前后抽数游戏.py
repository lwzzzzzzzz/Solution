# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/1 17:11
@Author:     wz
@File:       列表前后抽数游戏.py
@Decs:
"""

"""
有一个list，只能从列表的前后拿数，现有甲乙两人参与这个游戏，最终取数之和为甲乙的最终得分，得分大的获胜。
假设两人每步都能最大化拿数的收益，甲先取数，请问，给定list后，两人的得分是多少？

input: [1,4,10,3]
output: 甲：[1,10] 乙：[4,2]
"""


class Solution:
    """"
    该题考虑因为有两个人的存在，考虑两种情况，先手拿 和 后手拿
     1、该题有 暴力递归 和 动态规划 两种解法。
    """

    def __init__(self, nums):
        self.nums = nums

    def game(self):
        first, second = self.f(0, len(self.nums) - 1), self.s(0, len(self.nums) - 1)
        print("first score: {}; second score is: {}".format(first, second))

    def f(self, left, right):
        """
            先手函数
            1.base case当只有一个元素时，先手函数拿掉这个元素后直接返回
            2.当有多个元素时，先手函数可以取左右两边的任意一个，则取max(取左，取右)，同时取左或取右后，则变为后手
        """
        if left == right:
            return self.nums[left]

        return max(self.nums[left] + self.s(left + 1, right), self.nums[right] + self.s(left, right - 1))

    def s(self, left, right):
        """
            后手函数  ps：先后手只需要锁定一个人的视角，更好理解代码逻辑
            1.base case当只有一个元素时，后手函数则没有数可以拿，直接返回0
            2.当有多个元素时，因为是后手函数，先手必然会保留对后手最不利的情况，所以当前，我只有最小的可以取到，故min(取左，取右)，
                同时先手取完后，则变为先手
        """
        if left == right:
            return 0

        return min(self.f(left + 1, right), self.f(left, right - 1))


if __name__ == "__main__":
    nums = [1, 4, 11, 10, 3]
    s = Solution(nums)
    s.game()
