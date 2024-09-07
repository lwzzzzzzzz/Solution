# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/8 0:41
@Author:     wz
@File:       拷贝带随即指针的链表.py
@Decs:
"""
from LinkedList import RandomNode


class Solution:
    def function(self, head):
        if not head:
            return head

        h = dict()

        cur = head
        while cur:  # 用字典把所有节点先拷贝出来，并保存为 指向该节点的指针->节点 的格式
            h[cur] = RandomNode(cur.val)
            cur = cur.next

        cur = head
        # 拷贝节点之间的关系，因为字典内存的是 指向该节点的指针->节点，
        # 所以h[cur]找到当前节点，h[cur.next]和h[cur.random]找到当前节点的下一节点，之后再让字典内的节点相连，完成拷贝
        while cur:
            if cur.next:
                h[cur].next = h[cur.next]
            if cur.random:
                h[cur].random = h[cur.random]
            cur = cur.next
        return h[head]


if __name__ == "__main__":
    s = Solution()
