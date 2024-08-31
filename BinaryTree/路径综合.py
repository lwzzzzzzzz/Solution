# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 22:48
@Author:     wz
@File:       路径综合.py
@Decs:
"""
import collections

"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
"""


class Solution:
    # 暴力解法。对每一个节点都调用rootSum函数，递归找以每一个节点为起始节点的答案。
    def function(self, root, targetSum):
        def rootSum(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += rootSum(root.left, targetSum - root.val)
            ret += rootSum(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0

        res = rootSum(root, targetSum)  # 以当前节点为起始节点递归
        res += self.function(root.left, targetSum)
        res += self.function(root.right, targetSum)
        return res

    # 前缀和
    def pathSum(self, root, targetSum):
        prefix = collections.defaultdict(int)
        prefix[0] = 1

        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.val
            ret += prefix[curr - targetSum]
            prefix[curr] += 1
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1

            return ret

        return dfs(root, 0)


if __name__ == "__main__":
    s = Solution()
