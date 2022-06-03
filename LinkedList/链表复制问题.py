# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/7 0:22
@Author:     wz
@File:       链表复制问题.py
@Decs:
"""
from LinkedList import RandLinkedList

"""
给定一个特殊的单链表结构，其中每个单链表节点都有一个rand指针，指向单链表节点中任意一个节点，但是链表无环。
要求复制一个一样的链表结构。
"""


class Solution:
    def __init__(self, p):
        self.p = p

    def copy_given_linked_list(self):
        p = self.p
        return p


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    rl = RandLinkedList(nums)
    print(rl)
    head = rl.head.next

    head.rand = head.next.next
    head.next.rand = head.next.next.next.next
    print(rl)

