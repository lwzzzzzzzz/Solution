# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/24 0:08
@Author:     wz
@File:       递归构建二叉树.py
@Decs:
"""

from BinaryTree import Node

'''
递归方法构建一棵二叉树
'''

'''
包括 
1. 已知 <前序> <中序> 遍历
2. 已知 <后序> <中序> 遍历
3. 已知 <层序> <中序> 遍历
4. 一种特殊的 <序列化> <反序列化> 
四种情况构建二叉树
'''


# 4.<序列化> <反序列化> 其实就是把每一个节点的左右孩子（包括左右孩子为空的情况）都字符串化；和把已经字符化了的字符串 解析成一棵真正的树
def serial_tree_by_pre(node):
    if node is None:
        return "#_"

    res = (str(node.value) + "_")
    res += serial_tree_by_pre(node.left)
    res += serial_tree_by_pre(node.right)
    return res


# 反序列化
def deserial_tree_by_pre_str(pre_str):
    pre_list = pre_str.strip("_").split("_")
    print(pre_list)


def structure_tree_by_pre_str(pre_list):
    value = pre_list.pop(0)
    if value == "#":
        return

    n = Node(value)
    n.left = structure_tree_by_pre_str(pre_list)
    n.right = structure_tree_by_pre_str(pre_list)
    return n





if __name__ == "__main__":
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    head.left = n2
    head.right = n3
    n2.left = n4
    n3.right = n5
    n4.left = n6

    serial_pre_str = serial_tree_by_pre(head)
    print(serial_pre_str)
    deserial_tree_by_pre_str(serial_pre_str)

