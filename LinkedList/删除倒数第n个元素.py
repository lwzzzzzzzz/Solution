# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 23:45
@Author:     wz
@File:       删除倒数第n个元素.py
@Decs:
"""
from LinkedList import LinkedList, Node, print_linked


class Solution:
    """
    给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
    因为要删除节点，涉及到三个指针的操作，所以加一个dummy节点更为方便
    """
    def function(self, head, n):
        dummy = Node(0)
        dummy.next = head

        # 快指针往前n格
        fast = head
        for i in range(n):
            fast = fast.next

        # 同时移动快慢指针，满指针停下的位置就是要删除前元素位置
        slow = dummy
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 2, 1]
    linked = LinkedList(nums)
    head = linked.head.next
    l = s.function(head, 4)
    print_linked(l)
