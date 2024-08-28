# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/27 0:19
@Author:     wz
@File:       链表两两交换节点.py
@Decs:
"""
from LinkedList import LinkedList, print_linked, Node


class Solution:
    def function(self, head):
        dummy = Node(-1)
        dummy.next = head
        temp = dummy
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = node1

        return dummy.next


if __name__ == "__main__":
    nums1 = [1, 2, 3]
    linked1 = LinkedList(nums1)
    head1 = linked1.head.next
    print("first linkedList:", linked1)

    s = Solution()
    # print_linked(s.merge_two_linked(head1, head2))
    print_linked(s.function(head1))