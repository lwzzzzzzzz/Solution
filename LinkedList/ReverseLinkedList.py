# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/22 0:31
@Author:     wz
@File:       ReverseLinkedList.py
@Decs:
"""

from LinkedList import Node
from LinkedList import LinkedList


class Solution:
    def __init__(self, p):
        self.p = p

    def reverse(self):
        """
        很简单，准备三个指针 pre cur post，分别表示指向前一个节点的指针 / 指向当前节点的指针 / 指向后一个节点的指针
        """
        # 初始状态
        pre = None
        cur = self.p
        post = cur

        # 每次循环的起点都是cur和post同时指向当前节点；pre指向上一节点（未进入循环前则为空指针）
        # 因跳出循环的条件时cur为空指针，则说明pre已经到了原链表的最后一个节点，也就是说pre指向的是反转链表的第一个节点
        while cur:
            post = cur.next  # 先把指向下一个节点的指针保存
            cur.next = pre  # 当前节点指针反转
            # pre cur都往后走一位
            pre = cur
            cur = post
        return pre

        # # 初始状态
        # if self.p is None:
        #     return None
        #
        # pre = None
        # cur = self.p
        # post = cur.next
        #
        # # 每次循环的起点也可以是cur指向当前节点、post指向下一节点；pre指向上一节点（未进入循环前则为空指针）
        # # 但这样1、当传入链表节点为空时，要先判断；
        # #      2、因为每次循环进入的状态都是post在cur之后一个节点，当cur指向原链表最后一个节点时，post为null，循环内又要多判断一次
        # while cur:
        #     cur.next = pre  # 当前节点指针反转
        #     # pre cur都往后走一位
        #     pre = cur
        #     cur = post
        #     if post:
        #         post = post.next  # 把指向下一个节点的指针保存
        # return pre


if __name__ == "__main__":
    nums = [1, 2]
    linked = LinkedList(nums)
    p = linked.head.next
    print(linked)

    s = Solution(p)
    head = Node(None)
    head.next = s.reverse()  # 返回的链表需要在前面加一个头节点，以符合我们自定义的链表要求
    linked.head = head
    print(linked)
