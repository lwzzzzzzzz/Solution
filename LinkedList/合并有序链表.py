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


    # class Solution {
    #     把多个链表的list，通过分治的思想，最后拆分到索引对应的两两单链表的合并后，再逐层返回
    #     public ListNode mergeKLists(ListNode[] lists) {
    #         return merge(lists, 0, lists.length - 1);
    #     }
    #
    #     public ListNode merge(ListNode[] lists, int l, int r) {
    #         if (l == r) {
    #             return lists[l];
    #         }
    #         if (l > r) {
    #             return null;
    #         }
    #         int mid = (l + r) >> 1;
    #         return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r));
    #     }
    #
    #     public ListNode mergeTwoLists(ListNode a, ListNode b) {
    #         if (a == null || b == null) {
    #             return a != null ? a : b;
    #         }
    #         ListNode head = new ListNode(0);
    #         ListNode tail = head, aPtr = a, bPtr = b;
    #         while (aPtr != null && bPtr != null) {
    #             if (aPtr.val < bPtr.val) {
    #                 tail.next = aPtr;
    #                 aPtr = aPtr.next;
    #             } else {
    #                 tail.next = bPtr;
    #                 bPtr = bPtr.next;
    #             }
    #             tail = tail.next;
    #         }
    #         tail.next = (aPtr != null ? aPtr : bPtr);
    #         return head.next;
    #     }
    # }


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked1 = LinkedList(nums1)
    head1 = linked1.head.next
    print("first linkedList:", linked1)

    nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked2 = LinkedList(nums2)
    head2 = linked2.head.next
    print("first linkedList:", linked2)

    nums3 = [1, 2, 3, 4, 5, 6, 7, 8]
    linked3 = LinkedList(nums3)
    head3 = linked3.head.next
    print("first linkedList:", linked3)

    s = Solution()
    # print_linked(s.merge_two_linked(head1, head2))
    print_linked(s.merge_multi_order_linked([head1, head2, head3]))
