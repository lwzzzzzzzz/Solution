# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/16 23:34
@Author:     wz
@File:       二叉树是否是平衡二叉树.py
@Decs:
"""

from BinaryTree import Node, build_tree_from_level_order, print_vertical_tree


class Solution:
    """
    思路：两步 1. 任一节点有右孩子无左孩子时，直接返回false
              2. 在满足1条件的前提下，第一个叶子节点后面都是叶子节点
    """

    def __init__(self, head):
        self.head = head

    def is_balanced_binary_tree(self, ptr):
        if ptr is None:
            return True, 0

        is_left_avl, left_depth = self.is_balanced_binary_tree(ptr.left)
        left_depth = left_depth + 1
        is_right_avl, right_depth = self.is_balanced_binary_tree(ptr.right)
        right_depth = right_depth + 1

        # 当左右两树都是平衡二叉树，且包括当前节点后也是平衡二叉树，则当前树为平衡二叉树
        if is_left_avl and is_right_avl and abs(left_depth - right_depth) <= 1:
            is_avl = True
        else:
            is_avl = False
        return is_avl, max(left_depth, right_depth)


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 2, 4, 5, 5, 4])
    print_vertical_tree(head)

    s = Solution(head)
    print(s.is_balanced_binary_tree(head))
