# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/27 23:43
@Author:     wz
@File:       Traversal.py
@Decs:
"""

from BinaryTree import Node
from pythonds.basic.stack import Stack
import queue


def traversal(ptr, pattern="pre"):
    """
        前中后遍历递归实现
    """
    if ptr is None:
        return

    if pattern == "pre":
        print("pre_order node value:", ptr.value)

    traversal(ptr.left, pattern)
    if pattern == "in":
        print("in_order node value:", ptr.value)

    traversal(ptr.right, pattern)
    if pattern == "post":
        print("post_order node value:", ptr.value)


# 非递归实现
def loop_traversal(ptr, pattern="pre"):
    """
        用一个栈完美地模拟了递归的函数栈调用过程，即 先压左 -> 再压右 -> 出栈 的动态过程
        前中后序非递归实现
    """

    def push_left_node(ptr1):
        left = ptr1

        while left:
            if pattern == "pre":  # 先序遍历 即压栈前对其打印
                print(left.value)
            s1.push(left)
            left = left.left

    visited = Node(None)  # 引入visited节点，标识刚刚被访问过的子树的根节点
    s1 = Stack()

    # 先压左
    push_left_node(ptr)  # 首先遍历到左节点压栈直到节点为None，模拟递归当中永远先对左节点递归调用的操作，即：函数调用栈压栈的过程

    while not s1.isEmpty():

        node = s1.peek()
        # if （节点没有左节点了 或者 左边被访问了） && 右边没有被访问:
        #       node.left is None 条件表示节点没有左节点了，即此时就可以开始压栈右子树节点了
        if (node.left is None or node.left == visited) and node.right != visited:  # 条件缺一不可
            if pattern == "in":
                print("loop in_order node value:", node.value)
            push_left_node(node.right)  # 再压右

        # if 节点没有右节点了 或者 右边也被访问了:
        #       node.right is None 条件表示节点没有右节点了，而经过上一条if的判断，该节点左子树已经压过栈了，
        #                                 所以按照递归的调用栈逻辑，此时该节点应该被pop
        if node.right is None or node.right == visited:  # 条件缺一不可
            if pattern == "post":
                print("loop post_order node value:", node.value)
            visited = s1.pop()  # 出栈


def level_traversal(ptr, level=1, level_res=None):
    """
        层序遍历递归实现
    """
    if level_res is None:
        level_res = []
    if ptr is None:
        return

    if (level - 1) == len(level_res):  # 先序遍历的逻辑上，当满足此if条件，必然是第一次遍历访问到该层节点，所以需要先创建一个空list
        level_res.append([])
    level_res[level - 1].append(ptr.value)

    level_traversal(ptr.left, level + 1, level_res)
    level_traversal(ptr.right, level + 1, level_res)

    return level_res


def loop_level_traversal(ptr):
    """
        非递归层序遍历1
    """
    q = queue.Queue()
    level_map = dict()  # 记录每个节点所在的层数
    cur_level_width = 0  # 当前层宽度，初始化为0，当前还没有节点出队列
    cur_level = 1  # 当前所在层级，初始化为根节点第一层
    max_width = 0  # 记录的树最大宽度，
    if ptr:
        q.put(ptr)
        level_map[ptr] = 1

    while not q.empty():
        node = q.get()  # 节点出队后，进行统计和处理
        cur_node_level = level_map[node]  # 拿到当前节点所在层
        if cur_node_level == cur_level:  # 如果 当前节点所在层 等于 当前层 时，当前层宽度+1
            cur_level_width += 1
        else:  # 否则当前层遍历完成，此时这个节点是下一层的节点了，比较当前层宽度和已知前面层的最大宽度，进行比较，取较大值
            max_width = max(max_width, cur_level_width)
            cur_level += 1  # 当前层遍历完成，进入下一层
            cur_level_width = 1  # 当前层遍历完成，进入下一层，初始化为1，即这个节点被统计

        if node.left:
            q.put(node.left)
            level_map[node.left] = level_map[node] + 1  # 记录节点所在层数
        if node.right:
            q.put(node.right)
            level_map[node.right] = level_map[node] + 1  # 记录节点所在层数
    # print(level_map)
    print("max_width: ", max_width)


def loop_level_traversal2(ptr):
    """
        非递归层序遍历2
        强烈推荐这款
    """
    q = queue.Queue()
    max_width = 0
    level_res = []
    if ptr:
        q.put(ptr)

    while not q.empty():

        each_level_res = []
        max_width = max(max_width, q.qsize())
        for i in range(q.qsize()):  # 用此时队列的长度记住当前层节点有几个，则出栈几个节点
            node = q.get()
            each_level_res.append(node.value)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        level_res.append(each_level_res)
    print("max_width: ", max_width)
    return level_res
# def loop_traversal(ptr, pattern="pre"):
#     def push_left_node(ptr1):
#         p = ptr1
#
#         while p:
#             if pattern == "pre":  # 先序遍历 即压栈前对其打印
#                 print(p.value)
#             s1.push(p)
#             p = p.left
#
#     s1 = Stack()
#
#     push_left_node(ptr)  # 首先遍历到左节点压栈直到节点为None，模拟递归当中永远先对左节点递归调用的操作，即：函数调用栈压栈的过程
#
#     while not s1.isEmpty():
#
#         node = s1.peek()
#         s1.pop()
#
#         if pattern == "in":  # 先序遍历 即压栈前对其打印
#             print("in", node.value)
#         push_left_node(node.right)  # 再压右
#         # if pattern == "post":  # 先序遍历 即压栈前对其打印
#         #     print("post", node.value)



if __name__ == "__main__":
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    # n5 = Node(5)
    # n6 = Node(6)
    # n7 = Node(7)

    head.left = n2
    head.right = n3
    n2.left = n4
    # n3.right = n5
    # n4.left = n6
    # n4.right = n7

    # traversal(head, pattern="pre")
    # traversal(head, pattern="in")
    traversal(head, pattern="post")

    # loop_traversal(head, pattern="pre")
    # loop_traversal(head, pattern="in")
    loop_traversal(head, pattern="post")

    res = level_traversal(head)
    print(res)

    loop_level_traversal(head)
    res2 = loop_level_traversal2(head)
    print(res2)
