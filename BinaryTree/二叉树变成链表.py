# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/28 1:07
@Author:     wz
@File:       二叉树变成链表.py
@Decs:
"""
from BinaryTree import build_tree_from_level_order, print_vertical_tree


class Solution:
    """
        1. 最简单的方法是：前序遍历的时候把节点保存起来，然后再在保存好的list内遍历。修改二叉树的指针，使之成为链表
        2. 递归
        3. 迭代
            2、3的思路都是如下的过程，将左子树接到右节点，原来的右子树接在左子树的最右侧节点，完成一次拼接；
                然后一次迭代根节点的右子树root = root.right，直到root为null
             1         1          1
            /\          \          \
           2  5   ->     2     ->   2
          /\   \        / \          \
         3  4   6      3   4          3
                            \          \
                             5          4
                              \          \
                               6          5
                                           \
                                            6
    """
    def loop_flatten(self, root):
        cur = root
        while cur:
            if cur.left:  # 如果有左子树
                p = cur.left
                while p.right:
                    p = p.right  # 通过p找到该层左子树的最右侧节点
                p.right = cur.right  # 将root的右子树接在左子树的最右侧节点，
                cur.right = cur.left  # 将左子树搬到root的右节点
                cur.left = None  # 同时将root的左边置为null，完成一层迭代
            cur = cur.right  # 一层一层将左子树挂在右边
        return root


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 3, 4, 5, None, 7])
    print_vertical_tree(head)
    s = Solution()
    s.loop_flatten(head)
    print_vertical_tree(head)
