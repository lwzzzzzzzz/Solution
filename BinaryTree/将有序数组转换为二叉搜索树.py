# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/31 17:05
@Author:     wz
@File:       将有序数组转换为二叉搜索树.py
@Decs:
"""
from BinaryTree import Node

"""
给你一个整数数组nums，其中元素已经按升序排列，请你将其转换为一棵平衡二叉搜索树。
平衡二叉树的定义是，左右子树高度相差最多1，这样我们自然能想到左右两边都分布一半的元素，也就是分治，最后递归完成节点间的链接
"""

class Solution:
    def function(self, nums):

        def avl(nums, left, right):
            if left > right:  # 当等于的时候，还需要继续继续递归，为当前数字创建node
                return None
            mid = left + (right - left) // 2
            node = Node(nums[mid])
            node.left = avl(nums, left, mid - 1)
            node.right = avl(nums, mid + 1, right)
            return node

        avl(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    s = Solution()
    s.function(nums)
