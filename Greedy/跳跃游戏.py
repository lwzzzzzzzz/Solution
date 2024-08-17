# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/17 23:22
@Author:     wz
@File:       跳跃游戏.py
@Decs:
"""

'''
示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
'''


class Solution:
    def can_jump(self, nums):
        max_pos = 0
        for i in range(len(nums)):
            if max_pos < i:  # 如果当前遍历到的位置，通过遍历前面格子后，尽最大可能都不能达到max_pos，则不可能完成所有的跳跃
                return False
            max_pos = max(max_pos, i + nums[i])  # 每一步都京最大可能往前跳，当前位置能够超过现有的max_pos，则更新
        return True

    def step_cnt(self, nums):
        res = 0

        max_pos = 0
        start, end = 0, 0
        while end < len(nums) - 1:  # 当end能够到最后一个位置，则跳跃完成
            for i in range(start, end + 1):  # 一次跳跃，遍历可以接触到的所有格子，更新其max_pos
                max_pos = max(max_pos, i + nums[i])
            # 将上一次跳跃遍历完了的格子的下一个格子更新为下一次跳跃遍历的起点；下一个最远点更新为下一次跳跃遍历的起点
            start = end + 1
            end = max_pos
            res = res + 1  # 每次里层for循环完成一次，则完成了一次跳跃
        return res


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    s = Solution()
    print(s.can_jump(nums))
    print(s.step_cnt(nums))
