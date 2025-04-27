# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/26 0:34
@Author:     wz
@File:       合并有序链表.py
@Decs:
"""
from LinkedList import LinkedList, print_linked, Node


class Solution:
    def merge_two_linked(self, h1, h2):
        dummy = Node(-1)  # 定义一个dummy好操作链表
        pre = dummy
        while h1 and h2:
            if h1.value < h2.value:  # 让小于的节点直接和pre连接，此时上一个节点还连着，但因为下一次循环会断开，不做处理也可以
                pre.next = h1
                h1 = h1.next
            else:
                pre.next = h2
                h2 = h2.next
            pre = pre.next

        if h1:  # 处理后节点
            pre.next = h1
        if h2:
            pre.next = h2
        return dummy.next

    def merge_multi_order_linked(self, links):
        res = None
        for link in links:
            res = self.merge_two_linked(res, link)
        return res

    def merge_multi_order_linked_recursion(self, links):
        """
            递归实现合并多条有序链表。
            定义递归函数merge，该函数返回合并后的有序链表头节点。
            1. 当left == right相同时，说明递归边界，返回该条链表本身头节点
            2. 当left > right相同时，递归结束
            3. mid分治
            4. self.merge_two_linked完成合并左右两边链表的功能。之后return返回
        """
        def merge(left, right):
            if left == right:
                return links[left]
            if left > right:
                return

            mid = (left + right) >> 1
            return self.merge_two_linked(merge(left, mid), merge(mid + 1, right))

        return merge(0, len(links) - 1)


if __name__ == "__main__":
    s = Solution()

    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked1 = LinkedList(nums1)
    head1 = linked1.head.next
    print("linked1 linkedList:", linked1)

    nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked2 = LinkedList(nums2)
    head2 = linked2.head.next
    print("linked2 linkedList:", linked2)

    nums3 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked3 = LinkedList(nums3)
    head3 = linked3.head.next
    print("linked3 linkedList:", linked3)

    print_linked(s.merge_multi_order_linked([head1, head2, head3]))

    linked4 = LinkedList(nums1)
    head4 = linked4.head.next
    print("linked4 linkedList:", linked4)

    linked5 = LinkedList(nums2)
    head5 = linked5.head.next
    print("linked5 linkedList:", linked5)

    linked6 = LinkedList(nums3)
    head6 = linked6.head.next
    print("linked6 linkedList:", linked6)

    # print_linked(s.merge_two_linked(head1, head2))
    print_linked(s.merge_multi_order_linked_recursion([head4, head5, head6]))
