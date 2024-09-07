# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 1:27
@Author:     wz
@File:       两数相加.py
@Decs:
"""
from LinkedList import Node, LinkedList, print_linked

"""
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
"""


class Solution:
    def function(self, l1, l2):
        carry = 0
        dummy = Node(0)
        p3 = dummy
        p1, p2 = l1, l2
        while p1 or p2:  # 遍历到两个链表都为空
            if p1:  # 如果存在就取出值，否则置为0
                p1_val = p1.value
            else:
                p1_val = 0

            if p2:
                p2_val = p2.value
            else:
                p2_val = 0

            plus_value = p1_val + p2_val

            if carry > 0:  # 需要进位
                plus_value += 1  # 加上进位的1

            node_value = plus_value % 10  # 当前节点值
            carry = plus_value // 10  # 计算下次是否需要进位

            p3.next = Node(node_value)  # 结果链表
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            p3 = p3.next

        if carry > 0:  # 如果最后需要进位，则需要额外再加一个节点1
            p3.next = Node(1)

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    l1 = [2, 4, 5]  
    l2 = [5, 6, 4]

    linked1 = LinkedList(l1)
    head1 = linked1.head.next
    print("first linkedList:", linked1)
    linked2 = LinkedList(l2)
    head2 = linked2.head.next
    print("first linkedList:", linked2)
    ptr = s.function(head1, head2)
    print_linked(ptr)
