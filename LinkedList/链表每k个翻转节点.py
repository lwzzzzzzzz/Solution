# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/27 0:19
@Author:     wz
@File:       链表每k个翻转节点.py
@Decs:
"""
from LinkedList import LinkedList, print_linked, Node


class Solution:
    def reverse2Group(self, head):
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

    # 该方式为递归实现
    # 如果不递归实现的话，需要像reverse2Group一样，在K个节点内反转，记录头尾节点，再把这K个节点当作一个整体，做指针操作就行
    def reverseKGroup(self, head, k):
        # 当长度小于k时，直接返回
        cnt = 0
        p = head
        while p and cnt != k:  # 统计是否够长
            cnt += 1
            p = p.next
        if cnt < k:
            return head  # 不够长直接返回头节点head

        # 大于k时，需要反转链表后，头尾节点再连起来，返回链表k个节点的头
        pre, cur, post = None, head, head
        while cur != p:
            post = post.next
            cur.next = pre
            pre = cur
            cur = post
        # 需要与每次入参一致，也就是 (下一次递归的头节点指针，k)；
        # 同时此时已经反转了链表，所以head.next是把反转后的尾节点 和 子问题递归返回的头节点相连接
        head.next = self.reverseKGroup(post, k)
        return pre  # 返回反转后的头节点


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    linked1 = LinkedList(nums1)
    head1 = linked1.head.next
    print("first linkedList:", linked1)

    s = Solution()
    # print_linked(s.merge_two_linked(head1, head2))
    # print_linked(s.reverse2Group(head1))
    print_linked(s.reverseKGroup(head1, 3))
