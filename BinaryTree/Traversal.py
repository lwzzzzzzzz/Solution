# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/27 23:43
@Author:     wz
@File:       Traversal.py
@Decs:
"""

from BinaryTree import Node, print_vertical_tree, build_tree_from_level_order
import queue


def traversal(head1, pattern):
    def recursion_traversal(ptr):
        """
            前中后遍历递归实现
        """
        if ptr is None:
            return

        if pattern == "pre":
            res.append(ptr.value)

        recursion_traversal(ptr.left)
        if pattern == "in":
            res.append(ptr.value)

        recursion_traversal(ptr.right)
        if pattern == "post":
            res.append(ptr.value)

    res = []
    recursion_traversal(head1)
    return res


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


def loop_traversal(root, pattern="pre"):
    res = []
    cur, visited = root, None
    s1 = []
    while cur or s1:
        while cur:  # 左节点压栈
            if pattern == "pre":
                res.append(cur.value)  # 前序结果
            s1.append(cur)
            cur = cur.left

        cur = s1[-1]
        # 其实中序和后序都是一个过程，每个节点入栈出栈一次，只不过出栈的时间点不一样，遍历的结果就不一样
        if pattern == "in":
            s1.pop(-1)
            res.append(cur.value)  # 中序结果
            cur = cur.right  # 右节点压栈

        if pattern == "post":
            # 当右节点为空；或者右节点被访问过，也就是上一次出栈节点是右子节点。此时就是后序遍历出栈时间点
            if cur.right is None or cur.right == visited:
                s1.pop(-1)
                res.append(cur.value)  # 后序结果
                visited = cur
                cur = None  # cur如果不赋值给None，左节点又压栈了。。。
            else:  # 否则将右节点压栈
                cur = cur.right

        if pattern == "pre":
            s1.pop(-1)
            cur = cur.right
    return res


if __name__ == "__main__":
    head = build_tree_from_level_order([1, 2, 3, 4, 5, 6, 7])
    print_vertical_tree(head)

    print("pre_traversal: ", traversal(head, pattern="pre"))
    print("in_traversal: ", traversal(head, pattern="in"))
    print("post_traversal: ", traversal(head, pattern="post"))

    print("loop_pre_traversal: ", loop_traversal(head, pattern="pre"))
    print("loop_in_traversal: ", loop_traversal(head, pattern="in"))
    print("loop_post_traversal: ", loop_traversal(head, pattern="post"))

    print("level_traversal: ", level_traversal(head))
    print("loop_level_traversal2: ", loop_level_traversal2(head))
