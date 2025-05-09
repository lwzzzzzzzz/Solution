# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/16 22:42
@Author:     wz
@File:       二叉树是否是完全二叉树.py
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

    def is_complete_binary_tree(self):

        if self.head is None:
            return True

        ptr = self.head
        level_node = [ptr]
        cur_level = 1
        leaf = False

        while level_node:
            level_node_cnt = len(level_node)
            print("%s depth tree node_value: %s" % (cur_level, list(map(lambda n: n.value, level_node))))
            for i in range(level_node_cnt):
                node = level_node.pop(0)
                if node.left is not None:
                    level_node.append(node.left)
                if node.right is not None:
                    level_node.append(node.right)

                if (node.left is None and node.right is not None) \
                        or (leaf and (node.left is not None or node.right is not None)):  # 两个条件任意一个不满足即不是完全二叉树
                    return False

                if node.left is None and node.right is None:  # 此时node为第一个叶子节点，如果是完全二叉树，后续节点也应该是叶子节点
                    leaf = True  # 标记后续为叶节点

            cur_level += 1

        return True


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])
    print_vertical_tree(head)

    s = Solution(head)
    print(s.is_complete_binary_tree())
