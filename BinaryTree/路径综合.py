# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 22:48
@Author:     wz
@File:       路径综合.py
@Decs:
"""

from BinaryTree import build_tree_from_level_order, print_vertical_tree

"""
给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）
"""


class Solution:
    # 暴力解法。对每一个节点都调用root_sum函数，递归找以每一个节点为起始节点的答案。
    def exhaust_path_sum(self, root, target_sum):
        def root_sum(root, target_sum):
            if root is None:
                return 0

            ret = 0
            if root.value == target_sum:
                ret += 1
                # 这里不能res+1后，就直接return剪枝，因为后面可能会有0，有负数，加起来还等于target_sum的时候
            # 同理于为什么>或<，都不需要单独讨论

            ret += root_sum(root.left, target_sum - root.value)
            ret += root_sum(root.right, target_sum - root.value)
            return ret

        if root is None:
            return 0

        res = root_sum(root, target_sum)  # 以当前节点为起始节点递归
        res += self.exhaust_path_sum(root.left, target_sum)
        res += self.exhaust_path_sum(root.right, target_sum)
        return res

    # 前缀和
    def path_sum(self, root, target_sum):
        """
            思路：
            1.和一维数组的前缀和是一个一维数组一样；
              理论上来说prefix应该和原始的数据结构一样，也应该是一颗二叉树，但是此题不要求返回路径，只要求求出路径个数，所以简化成了前缀和：cnt的kv对
            2.prefix二叉树前缀和意义：prefix[Y]是从根节点到当前节点的前缀和为Y的个数
            从X到Y的路径和为 prefix[Y]-prefix[X]，题意为找到满足 prefix[Y]-prefix[X]=target_sum 的个数
            换一种说法就是 “当到达到Y节点，前缀和数组prefix中值等于 prefix[Y]-target_sum 的个数”
        """
        def dfs(root, curr):
            if not root:
                return 0

            ret = 0
            curr += root.value  # 从根节点到当前节点的前缀和
            ret += prefix.get(curr - target_sum, 0)  # 如果prefix[Y]-target_sum存在，那么更新ret
            prefix[curr] = prefix.get(curr, 0) + 1  # 更新prefix[Y]
            ret += dfs(root.left, curr)
            ret += dfs(root.right, curr)
            prefix[curr] -= 1  # 回溯时将当前前缀和的计数减1
            return ret

        prefix = dict()
        prefix[0] = 1
        return dfs(root, 0)


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 2, 4, 3, 6, 7])
    print_vertical_tree(head)
    s = Solution()
    print(s.path_sum(head, 3))
    print(s.exhaust_path_sum(head, 3))
