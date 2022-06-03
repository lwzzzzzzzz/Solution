# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/17 0:08
@Author:     wz
@File:       二叉树是不是搜索二叉树.py
@Decs:
"""
import sys
from BinaryTree import Node


class Solution:
    """
    思路：中序遍历严格递增则为搜索二叉树
    """

    def __init__(self, head):
        self.head = head
        self.pre_value = -sys.maxsize

    def is_binary_search_tree(self, ptr):
        if ptr is None:
            return True

        is_left_bst = self.is_binary_search_tree(ptr.left)
        # 左树为非搜索二叉树时，自然直接返回false
        if is_left_bst is False:
            return False

        if ptr.value <= self.pre_value:  # 如果在当前节点不满足搜索二叉树的要求，即节点值小于等于左孩子值，则不需要递归遍历右子树 可直接返回False；
            return False
        else:  # 否则将当前值设置为前一节点值，进入到右子树判断
            self.pre_value = ptr.value
        return self.is_binary_search_tree(ptr.right)

    def is_binary_search_tree2(self, ptr):
        """
        这题拆分为子问题，需要直到左子树是否为搜索二叉树，左子树的最大值；右子树是否为搜索二叉树，右子树的最小值；
            当不使用全局变量的时候，我们要把这个问题拆解成递归可以解的问题，但是左右子问题又不完全一致，
            此时把问题再处理一下，同时对左右子树都求最大值和最小值，全部依靠递归返回即可。
        """
        if ptr is None:
            return None, None, None

        is_left_bst, left_max_value, left_min_value = self.is_binary_search_tree(ptr.left)
        is_right_bst, right_max_value, right_min_value = self.is_binary_search_tree(ptr.right)

        #  当前树的最大最小值
        mi = ptr.value
        ma = ptr.value
        if left_min_value is not None:
            ma = max(left_max_value, ma)
            mi = min(left_min_value, mi)
        if right_min_value is not None:
            ma = max(right_max_value, ma)
            mi = min(right_min_value, mi)

        is_bst = True  # 默认为True，根据状态确定不是的情况
        if is_left_bst is not None:  # 当 当前左树返回不为空时，左树已经不是搜索二叉树；或者左边最大值大于等于当前值，不是搜索二叉树返回False
            if is_left_bst is False or (is_left_bst is True and left_max_value >= ptr.value):
                is_bst = False

        if is_right_bst is not None:  # 同上
            if is_right_bst is False or (is_right_bst is True and ptr.value >= right_min_value):
                is_bst = False
        return is_bst, ma, mi


if __name__ == "__main__":
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    # n5 = Node(5)
    # n6 = Node(6)
    # n7 = Node(7)

    head.right = n2
    head.left = n3
    n2.left = n4
    # n3.right = n5
    # n4.left = n6
    # n4.right = n7

    s = Solution(head)
    print(s.is_binary_search_tree(head))
