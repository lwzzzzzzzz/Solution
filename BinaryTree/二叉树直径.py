# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/5 1:57
@Author:     wz
@File:       二叉树直径.py
@Decs:
"""


class Solution:
    """
        直径定义，最长链的边长，如：
              2
             / \
            1   3
           /\   /\
          4  5 6  7
        其中最长的链为 4-1-2-3-7 则有4条边，直径为4
    """
    def diameterOfBinaryTree(self, root):
        diameter = []
        self.recursion_depth(root, diameter)
        return max(diameter)

    def recursion_depth(self, p, diameter):
        if p is None:
            return 0

        l = self.recursion_depth(p.left, diameter)
        r = self.recursion_depth(p.right, diameter)
        cur_node_path = l + r  # 对于当前节点，直径为：左边深度 + 1 + 右边深度 - 1
        diameter.append(cur_node_path)

        depth = max(l, r) + 1
        return depth

    # 当不存所有节点的直径
    # self.ans = 0
    # def recursion_depth(p):
    #     if p is None:
    #         return 0

    #     l_depth = recursion_depth(p.left)
    #     r_depth = recursion_depth(p.right)
    #     self.ans = max(self.ans, l_depth + r_depth)

    #     depth = max(l_depth, r_depth) + 1
    #     return depth

    # depth = recursion_depth(root)
    # return self.ans


if __name__ == "__main__":
    s = Solution()
