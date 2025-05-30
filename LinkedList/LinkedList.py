# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/22 0:31
@Author:     wz
@File:       LinkedList.py
@Decs:
"""

"""链表类/方法"""


def print_linked(head):
    p = head
    s = ""
    if p is None:
        print("input linked list is empty")
    while p:
        s += str(p.value) + " "
        p = p.next
    print(s)


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class RandomNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.random = None


class LinkedList:
    def __init__(self, nums):
        self.head = Node(None)
        self.initial(nums)

    def initial(self, nums):
        p = self.head
        for i in nums:
            p.next = Node(i)
            p = p.next

    def __str__(self):
        s = ""
        p = self.head.next
        while p:
            s += str(p.value) + " "
            p = p.next
        return s
    # def add(self, node):
    #     self.head.next = node


class RandNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.rand = None
