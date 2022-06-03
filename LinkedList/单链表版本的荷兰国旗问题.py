# _*_ coding: utf-8 _*_
"""
@Date:       2022/3/2 0:34
@Author:     wz
@File:       单链表版本的荷兰国旗问题.py
@Decs:
"""
from LinkedList import LinkedList

"""
问题描述：给定一个数值target，和一个单链表，将其组织成小于target再左侧，等于target在中间，大于target在右侧，并保证其稳定性
如 target=2  4->2->3->2->1 返回为：1->2->2->4->3
"""

def print_linked(p):
    s = ""
    while p:
        s += str(p.value) + " "
        p = p.next
    print(s)

class Solution:
    def __init__(self, p):
        self.p = p

    def small_given_big_rank(self, given):
        """
        思路很简单，就是用三个头指针保存小于、等于、大于三种状态的开始，三个尾指针保存小于、等于、大于三种状态的结尾，最后合并
            此题难点在于：小于、等于、大于三种状态的合并，需要讨论三者是否存在的情况。
        """
        small, equal, big = None, None, None
        small_tail, equal_tail, big_tail = None, None, None

        p = self.p
        while p:
            if p.value < given:
                if not small:
                    small, small_tail = p, p
                else:
                    small_tail.next = p
                    small_tail = small_tail.next
            elif p.value == given:
                if not equal:
                    equal, equal_tail = p, p
                else:
                    equal_tail.next = p
                    equal_tail = equal_tail.next
            else:
                if not big:
                    big, big_tail = p, p
                else:
                    big_tail.next = p
                    big_tail = big_tail.next

            p = p.next

        # 跳出循环后，三个状态的尾指针都还彼此连着直到链表尾，因为三种状态的尾指针都未将该节点设置为null，而是维持着原链表的连接，
        #      但是这不要紧，因为最后我们都需要把它们串起来，改变其指向
        # small_tail.next, equal_tail.next, big_tail.next = None, None, None
        print_linked(small)
        print_linked(equal)
        print_linked(big)

        # 链接三种状态的头尾指针，讨论各种条件
        if small_tail is not None:
            small_tail.next = equal
            if equal_tail is None:
                equal_tail = small_tail
            else:
                equal_tail = equal_tail

        if equal_tail is not None:
            equal_tail.next = big_tail

        if small is not None:
            return small
        if equal is not None:
            return equal
        return big


        return p


if __name__ == "__main__":
    nums = [4, 2, 3,2, 1]
    linked = LinkedList(nums)
    head = linked.head.next
    print_linked(head)

    s = Solution(head)
    print(s.small_given_big_rank(2))
