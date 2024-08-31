# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 1:06
@Author:     wz
@File:       组合总和.py
@Decs:
"""

"""
给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
"""

class Solution:
    def function(self, candidates, target):
        res = []

        def dfs(t, path, start):
            if t == 0:
                res.append(path[:])
                return
            if t < 0:
                return

            # 这个位置for循环表示可选取的元素，通过dfs(t - candidates[i], path, i)的i控制，避免重复
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # 这里dfs(t - candidates[i], path, i)的i，表示可以重复取当前元素；
                # 如果是像“所有子集”那题，backtrack(nums, i + 1, path)，i+1 表示一个元素只能被取一次
                dfs(t - candidates[i], path, i)
                path.pop(-1)
        dfs(target, [], 0)
        return res


if __name__ == "__main__":
    s = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(s.function(candidates, target))

