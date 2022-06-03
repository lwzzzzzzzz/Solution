# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/20 19:10
@Author:     wz
@File:       两条单链表交叉问题.py
@Decs:
"""

'''
给定两条单链表，两条单链表可以有环 也可以无环，请问这两条单链表是否交叉，如交叉，返回交叉节点指针；如不交叉，返回空
'''

from LinkedList import *


def make_loop(head, in_loop):
    p = head
    while p.next:
        p = p.next

    tmp = head
    while in_loop > 0:  # 把头节点后in_loop个节点当作入环点
        in_loop -= 1
        tmp = tmp.next
    p.next = tmp
    print("入环点: ", p.next.value)

    # tmp = head
    # while tmp != p:
    #     print(tmp.value, end=" ")
    #     tmp = tmp.next
    # print(tmp.value)
    return p.next


def is_loop(head):
    if head is None or head.next is None:
        return None
    slow, fast = head.next, head.next.next
    while slow != fast:
        if fast.next is None or fast.next.next is None:  # 如无环fast先到尾部，并返回None
            return None
        slow = slow.next
        fast = fast.next.next
    # 当运行到此处时，说明链表有环
    print("linkedList has circle")

    # 此时让快指针回到链表头，同时快慢指针都以1的速度往下走，再一次遇见时即为链表环入口
    fast = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    return fast


class Solution:
    """
    我们可以分为三种情况：
        1、两个链表都无环（其中分为两种情况）
            1.1 无环无交叉点
            1.2 无环有交叉点（即Y形链表）
        2、其中一个链表有环 一个链表无环
            这种时候不可能有交叉点，可以自己画一画
        3、两个链表都有环（其中又分为三种情况）
            3.1 都有环但无交叉点
            3.2 都有环交叉点在入环点之前
            3.3 都有环交叉点在环内
    """
    def __init__(self, h1, h2):
        self.head1 = h1
        self.head2 = h2
        self.in_loop_node1 = is_loop(self.head1)  # 链表入环点
        self.in_loop_node2 = is_loop(self.head2)

    def cross_node(self):
        if self.head1 is None or self.head2 is None:
            return None
        if self.in_loop_node1 is None and self.in_loop_node2 is None:
            return self.get_no_loop_cross_node()
        if self.in_loop_node1 and self.in_loop_node2:
            return self.get_loop_cross_node()
        return None

    def get_no_loop_cross_node(self):
        p1, p2 = self.head1, self.head2
        len1, len2 = 1, 1
        while p1.next:
            len1 += 1
            p1 = p1.next
        while p2.next:
            len2 += 1
            p2 = p2.next

        if p1 != p2:  # 当最后一个节点都不一样时，两单链表必不可能相交
            return None

        p1, p2 = self.head1, self.head2

        # 根据长度让长的那条链表多走一会，使之后走相同步数可以到达交叉点，此时相等跳出循环，并返回
        if len1 > len2:
            while len1 > len2:
                len1 -= 1
                p1 = p1.next
        else:
            while len2 > len1:
                len2 -= 1
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1


    def get_loop_cross_node(self):
        # 当出现3.2的情况，其实和无环情况是一样的，只是把最后节点都换成入环节点
        p1, p2 = self.head1, self.head2
        len1, len2 = 1, 1
        if self.in_loop_node1 == self.in_loop_node2:
            while p1.next != self.in_loop_node1:
                len1 += 1
                p1 = p1.next
            while p2.next != self.in_loop_node2:
                len2 += 1
                p2 = p2.next

            p1, p2 = self.head1, self.head2

            # 根据长度让长的那条链表多走一会，使之后走相同步数可以到达交叉点，此时相等跳出循环，并返回
            if len1 > len2:
                while len1 > len2:
                    len1 -= 1
                    p1 = p1.next
            else:
                while len2 > len1:
                    len2 -= 1
                    p2 = p2.next

            while p1 != p2:
                p1 = p1.next
                p2 = p2.next
            return p1  # 返回3.2情况


        # 为区分3.1和3.3的情况，只需要以一个入环点绕一圈，假设绕链表1的环途中发现，有链表环2的入环点，说明两者的交叉点为整个环，则最近的交叉点为链表1或2的入环点均可
        circle_flag = self.in_loop_node1.next
        while circle_flag != self.in_loop_node1:
            if circle_flag == self.in_loop_node2:
                return self.in_loop_node1  # 返回 3.3的情况
        # 否则返回3.1情况
        return None


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked1 = LinkedList(nums1)
    head1 = linked1.head.next
    print("first linkedList:", linked1)
    in_loop_node1 = make_loop(head1, 4)
    # print(in_loop_node1.value)
    # print("function return in_loop_node:", is_loop(head1).value)

    nums2 = [9, 10, 11, 12, 13, 14, 15, 16]
    linked2 = LinkedList(nums2)
    head2 = linked2.head.next
    print("second linkedList:", linked2)
    in_loop_node2 = make_loop(head2, 4)
    # print(in_loop_node2.value)

    nums3 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked3 = LinkedList(nums3)
    head3 = linked3.head.next
    print("third linkedList:", linked3)
    # print(is_loop(head3))

    nums4 = [9, 10, 11, 12, 13, 14, 15, 16]
    linked4 = LinkedList(nums4)
    head4 = linked4.head.next
    print("fourth linkedList:", linked4)
    p4 = head4
    while p4.next:
        p4 = p4.next
    p4.next = head3
    print("after fourth linkedList:", linked4)

    s = Solution(head3, head3)
    print(s.cross_node().value)
