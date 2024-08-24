# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 0:12
@Author:     wz
@File:       tes.py
@Decs:
"""
import collections


class Solution:
    def inorderTraversal(self, root):
        res = []
        cur = root
        s1 = []
        while cur or s1:
            while cur:
                s1.append(cur.val)
                cur = cur.left
            node = s1[-1]
            s1.pop(-1)
            res.append(node.val)
            cur = cur.right
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function("abcc")
    print(xxx)
