# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 0:12
@Author:     wz
@File:       tes.py
@Decs:
"""
import collections


class Solution:
    def function(self, nums, k):
        tmp = [[] for _ in range(len(nums) + 1)]
        print(tmp)
        d1 = dict()
        for i in range(len(nums)):
            if nums[i] in d1.keys():
                d1[nums[i]] = d1[nums[i]] + 1
            else:
                d1[nums[i]] = 1

        print(d1)
        for key, value in d1.items():
            tmp[value].append(key)
        print(tmp)

        res = []
        for i in range(len(tmp) - 1, -1, -1):
            for num in tmp[i]:
                if len(res) < k:
                    res.append(num)
                else:
                    break
            if len(res) == k:
                break
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    xxx = s.function(nums, k)
    print(xxx)
