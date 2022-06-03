# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/28 0:04
@Author:     wz
@File:       单链表是否回文.py
@Decs:
"""
from LinkedList import LinkedList
from LinkedList import Node
import queue

"""
问题描述：给定一个链表，问此链表是否回文
如：1->2->3->2->1 返回True; 1->2->2->1 返回True; 1->2->2 返回False; 
"""
def reverse(head):
    pre = None
    cur, post = head, head
    while cur:
        post = post.next
        cur.next = pre
        pre = cur
        cur = post
    return pre


def print_linked(p):
    s = ""
    while p:
        s += str(p.value) + " "
        p = p.next
    print(s)


class Solution:

    def __init__(self, p):
        self.p = p

    def is_palindrome1(self):
        """
        方法一：最简单的方法，直接整一个栈，丢进去，再比对出栈元素和遍历元素是否相等，有不相等则返回false
        O(N) O(N)
        """
        stack = queue.LifoQueue()
        p = self.p
        while p:
            stack.put(p.value)
            p = p.next

        p = self.p
        while not stack.empty():
            if p.value != stack.get():
                return False
            p = p.next
        return True

    def is_palindrome2(self):
        """
        方法二：其实只需要将一半元素放入栈内，对比另一半元素和入栈的那一半是否相等，有不相等则返回false
        O(N) O(N)
            该方法的重点是首先如何找到单链表的中点让其中一般元素入栈，这里用快慢指针完成
        """

        fast, slow = self.p, self.p
        # 当fast遍历完成时，slow指针正好在下半段的前一个节点位置。更详细地说：
        #       1、当链表长度为奇数时，slow指针停在正中间。1->2->3->2->1  此时slow停在3位置
        #       2、当链表长度为偶数时，slow指针停在上半段最后。1->2->3->4  此时slow停在2位置
        while fast.next and fast.next.next:  # 两个条件，处理链表长度为奇数偶数的情况
            fast = fast.next.next
            slow = slow.next

        stack = queue.LifoQueue()
        p = slow.next
        while p:
            stack.put(p.value)
            p = p.next

        p = self.p
        while not stack.empty():
            if p.value != stack.get():
                return False
            p = p.next
        return True

    def is_palindrome3(self):
        """
        方法三：我们在之前的学习中，有接触到将链表反转，那么我们可以先找到链表中点，对后面的链表反转，再将前半部分和后半部分一一比对即可。
        O(N) O(1)
        """

        is_palindrome = True
        # 先找中点
        p, fast, slow = self.p, self.p, self.p
        # slow_slow = None
        while fast.next and fast.next.next:
            # slow_slow = slow
            fast = fast.next.next
            slow = slow.next
        # print_linked(slow_slow)
        behind = slow.next  # 后半部分的指针
        reverse_behind = reverse(behind)  # 反转后半部分，返回反转后的头指针，此时链表从behind处已经断开

        tmp = reverse_behind
        while tmp:  # 遍历已反转的后半段链表 并进行比对
            if tmp.value != p.value:
                is_palindrome = False
                break
            tmp = tmp.next
            p = p.next

        slow.next = reverse(reverse_behind)  # 把后半部分被反转的链表反转回来，再把断了的链表接上
        return is_palindrome


if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1]
    linked = LinkedList(nums)
    head = linked.head.next
    print(linked)

    s = Solution(head)
    print(s.is_palindrome1())
    print(s.is_palindrome2())
    print(s.is_palindrome3())
    print(linked)
