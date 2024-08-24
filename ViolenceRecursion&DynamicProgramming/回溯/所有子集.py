# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 18:05
@Author:     wz
@File:       所有子集.py
@Decs:
"""

"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""


class Solution:
    def function(self, nums):
        res = []

        def backtrack(nums, index, path):
            # 为什么在回溯的时候，这里不需要有任何的判断条件？
            # 原因在于子集和全排列不同，子集是回溯树中的每一个节点都是res的解，而全排列只有到达叶子节点时才是题解！！！
            res.append(path[:])
            if index >= len(nums):
                return

            print(res)
            for i in range(index, len(nums)):
                path.append(nums[i])
                backtrack(nums, i + 1, path)  # 因为子集定义要求不重复，所以从i+1开始
                path.pop(-1)

        backtrack(nums, 0, [])
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.function([1, 2, 3]))
