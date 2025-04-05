# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/6 1:14
@Author:     wz
@File:       向二叉搜索树插入元素.py
@Decs:
"""

from BinaryTree import Node, build_tree_from_level_order, print_vertical_tree

'''
    该题递归修改二叉树典中典，不再是递归查询或遍历了，而是需要修改。
        1、这个时候就需要通过递归找到要修改的节点位置
        2、新建需要插入的节点并返回该节点的指针
        3、考虑好当没有找到要修改位置的返回，即最后位置的返回，该题时输入是啥就输出啥
'''
class Solution:
    def insert_into_bst(self, root, val: int):
        return self.recursion_insert_into_bst(root, val)

    def recursion_insert_into_bst(self, root, val):
        if root is None:  # 当根据二叉搜索树的定义找到这个位置时，就是应该插入的位置
            return Node(val)

        if root.value > val:
            root.left = self.recursion_insert_into_bst(root.left, val)
        else:
            root.right = self.recursion_insert_into_bst(root.right, val)

        return root  # 返回root，输入是啥输出就是啥，结合上面的if root is None: ，意思就是当没有找到要插入的节点位置时，不做任何改变


if __name__ == "__main__":
    s = Solution()
    head = build_tree_from_level_order([9, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13])
    print_vertical_tree(head)
    s.insert_into_bst(head, 8)
    print_vertical_tree(head)
