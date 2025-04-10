# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/18 0:21
@Author:     wz
@File:       二叉树是否为满二叉树.py
@Decs:
"""

from BinaryTree import Node, print_vertical_tree, build_tree_from_level_order


class Solution:
    """
    两种思路：1.层序遍历，数每一层是否都是 2^(层数-1) 个节点
            2.前中后序遍历，看树总节点个数是否是 2^(层数)-1 个
    """

    def __init__(self, head):
        self.head = head

    def is_full_binary_tree(self):

        if self.head is None:
            return True

        ptr = self.head
        level_node = [ptr]
        cur_level = 1

        while level_node:
            level_node_cnt = len(level_node)
            print("%s depth tree node_value: %s" % (cur_level, list(map(lambda n: n.value, level_node))))
            if level_node_cnt == 2 ** (cur_level - 1):
                for i in range(level_node_cnt):
                    node = level_node.pop(0)
                    if node.left is not None:
                        level_node.append(node.left)
                    if node.right is not None:
                        level_node.append(node.right)
            else:
                return False
            cur_level += 1

        return True

    def is_full_binary_tree2(self):
        tree_node_cnt, tree_depth = (self.binary_tree_info(self.head))
        print("tree_depth: %s, tree_node_cnt: %s" % (tree_depth, tree_node_cnt))
        return tree_node_cnt == 2 ** tree_depth - 1

    def binary_tree_info(self, ptr):
        if ptr is None:
            return 0, 0

        left_cnt, left_depth = self.binary_tree_info(ptr.left)
        right_cnt, right_depth = self.binary_tree_info(ptr.right)

        return left_cnt + right_cnt + 1, max(left_depth, right_depth) + 1


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])
    print_vertical_tree(head)

    s = Solution(head)
    print(s.is_full_binary_tree())
    print(s.is_full_binary_tree2())
