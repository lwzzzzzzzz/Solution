# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/12 13:36
@Author:     wz
@File:       二叉树是否是对称.py
@Decs:
"""
from BinaryTree import Node


class Solution:
    def is_symmetrical_tree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        # if p.value != q.value:
        #     return False

        # 根据对称的定义，无非是
        #   1、当前节点的左节点和镜像节点的右节点
        #   2、当前节点的右节点和镜像节点的左节点
        #   结构和值一样  ps：通过 下两句递归遍历 和 前两个if 校对结构；p.value != q.value校对值
        is_sub_symmetrical_tree1 = self.is_symmetrical_tree(p.left, q.right)
        is_sub_symmetrical_tree2 = self.is_symmetrical_tree(p.right, q.left)

        # if is_sub_symmetrical_tree1 and is_sub_symmetrical_tree2:
        #     return True

        # p.value == q.value条件放在先序和后序没有本质区别，区别在于等对应节点值不一样的时候，不需要再去校对结构是否一致
        if is_sub_symmetrical_tree1 and is_sub_symmetrical_tree2 and p.value == q.value:
            return True
        else:
            return False


if __name__ == "__main__":
    s = Solution()
    head = Node(1)
    n2 = Node(2)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(3)

    head.left = n2
    head.right = n3
    n3.left = n4
    n2.right = n5
    print(s.is_symmetrical_tree(head, head))
