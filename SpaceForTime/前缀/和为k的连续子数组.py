# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/22 1:22
@Author:     wz
@File:       和为k的连续子数组.py
@Decs:
"""


class Solution:
    def function(self, nums: list[int], k: int) -> int:
        # 前缀和最简单的构造方式
        # prefix_sum = [0] * (len(nums) + 1)
        # for i in range(1, len(prefix_sum)):
        #     prefix_sum[i] = prefix_sum[i-1] + nums[i-1]
        # print(prefix_sum)

        res, pre_sum = 0, 0
        pre_sum_dict = dict()
        pre_sum_dict[0] = 1
        for i in range(len(nums)):
            pre_sum += nums[i]
            # 利用前缀和数组 pre_sum_j - pre_sum_i = 某子序列和k 的性质，
            # 如果 pre_sum_j - 某子序列和k 在pre_sum_dict内，说明存在子序列和为k，res加上pre_sum - k出现次数
            if pre_sum - k in pre_sum_dict.keys():
                res += pre_sum_dict[pre_sum - k]

            if pre_sum in pre_sum_dict.keys():  # 存储所有前缀和
                pre_sum_dict[pre_sum] += 1
            else:
                pre_sum_dict[pre_sum] = 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.function([1, 2, 1, 3, 4], 3))
