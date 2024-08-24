# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 17:34
@Author:     wz
@File:       数组全排列.py
@Decs:
"""

"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""
class Solution:
    def function(self, nums):
        res = []

        def backtrack(nums, path):
            if len(path) == len(nums):
                res.append(path[:])  # s1[:]实现深拷贝数组
                return

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                backtrack(nums, path)
                path.pop(-1)

        backtrack(nums, [])
        return res





if __name__ == "__main__":
    s = Solution()
    print(s.function([1, 2, 3]))
