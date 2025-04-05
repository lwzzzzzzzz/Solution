# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/27 23:44
@Author:     wz
@File:       BinaryTree.py
@Decs:
"""
import matplotlib.pyplot as plt
import networkx as nx


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def build_tree_from_level_order(level_order):
    if not level_order or level_order[0] is None:
        return None

    root = Node(level_order[0])
    queue = [root]  # 用列表代替deque
    idx = 1

    while queue and idx < len(level_order):
        current_node = queue.pop(0)  # 注意这里用pop(0)模拟队列，时间复杂度O(n)

        # 处理左子节点
        if idx < len(level_order) and level_order[idx] is not None:
            current_node.left = Node(level_order[idx])
            queue.append(current_node.left)
        idx += 1

        # 处理右子节点
        if idx < len(level_order) and level_order[idx] is not None:
            current_node.right = Node(level_order[idx])
            queue.append(current_node.right)
        idx += 1

    return root


def print_vertical_tree(root):
    def get_height(node):
        if not node:
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    height = get_height(root)
    max_level = height - 1
    # 计算需要的宽度：最后一层有2^(h-1)个节点，每个节点至少3个字符宽
    last_level_width = 2 ** (height - 1) * 3 - 1
    res = [[" " for _ in range(last_level_width)] for _ in range(2 * height - 1)]

    def fill(node, level, left, right):
        if not node:
            return

        mid = (left + right) // 2
        val_str = str(node.value)
        # 将节点值放在中间
        start = mid - len(val_str) // 2
        res[level][start:start + len(val_str)] = list(val_str)

        if node.left:
            # 计算左子节点的位置
            left_mid = (left + mid) // 2
            # 画左斜线
            res[level + 1][left_mid] = '/'
            # 画连接线
            for i in range(left_mid + 1, mid):
                res[level + 1][i] = ' '
            fill(node.left, level + 2, left, mid - 1)

        if node.right:
            # 计算右子节点的位置
            right_mid = (mid + 1 + right) // 2
            # 画右斜线
            res[level + 1][right_mid] = '\\'
            # 画连接线
            for i in range(mid + 1, right_mid):
                res[level + 1][i] = ' '
            fill(node.right, level + 2, mid + 1, right)

    fill(root, 0, 0, last_level_width - 1)

    for line in res:
        print(''.join(line))
    print("-"*30)


def visualize_tree(root):
    G = nx.Graph()
    pos = {}

    def add_edges(node, x=0, y=0, layer=1):
        if node is not None:
            G.add_node(node.value)
            pos[node.value] = (x, y)

            if node.left:
                G.add_edge(node.value, node.left.value)
                l = x - 1 / (2 ** layer)
                add_edges(node.left, x=l, y=y - 1, layer=layer + 1)

            if node.right:
                G.add_edge(node.value, node.right.value)
                r = x + 1 / (2 ** layer)
                add_edges(node.right, x=r, y=y - 1, layer=layer + 1)

    add_edges(root)

    plt.figure(figsize=(8, 5))
    nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title("Binary Tree Visualization")
    plt.show()

