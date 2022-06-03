# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/22 0:31
@Author:     wz
@File:       LinkedList.py
@Decs:
"""

"""链表类"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


class RandLinkedList:
    def __init__(self, nums):
        self.head = RandNode(None)
        self.initial(nums)

    def initial(self, nums):
        p = self.head
        for i in nums:
            p.next = RandNode(i)
            p = p.next

    def __str__(self):
        s = ""
        p = self.head.next
        while p:
            s += 'value: ' + str(p.value) + ", "
            if p.rand:
                s += 'randValue: ' + str(p.rand.value) + "; "
            p = p.next
        return s
    # def add(self, node):
    #     self.head.next = node
