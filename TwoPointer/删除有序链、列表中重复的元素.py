# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/5 0:39
@Author:     wz
@File:       删除有序链、列表中重复的元素.py
@Decs:
"""
from LinkedList.LinkedList import LinkedList
from LinkedList.LinkedList import print_linked

class Solution:
    """
        双指针，链表和列表之间有一定区别，以体现在注释中
        ps：此题并不是荷兰国旗问题，荷兰国旗问题针对一个给定的数值去进行各种规则的排序，但框架一样，考虑清楚左指针的意义就能ac
    """
    def deleteDuplicates(self, head):
        reserve, p = head, head  # reserve指示已处理的最后一个不重复元素；p遍历链表

        if head is None:
            return head

        while p:  # 该题思路与list一致，用一个指针保存下一个要插入的节点位置，另一个遍历链表
            if p.value != reserve.value:
                # 找到新的不重复元素，将其放到先前最后一个不重复元素，它就成为新的最后一个不重复元素
                reserve.next = p  # list通过swap完成去重；链表通过修改指针指向完成
                reserve = reserve.next
            p = p.next

        # 当出现了x -> 1 -> 1 -> 1这类情况，根据上面的代码，reserve指向第一个1位置，并不能后面重复的元素，所以此时链表需要截断
        # 只不过和list的不同在于，list种reserve指针下标记录有多少个不重复的数字，最后nums[:cnt+1]截断即可；链表通过reserve.next = None截断
        if reserve.next is not None:
            reserve.next = None
        return head

    def removeDuplicates(self, nums):
        reserve, i = 0, 0  # reserve指示已处理的最后一个不重复元素；i遍历列表
        while i < len(nums):
            if nums[i] != nums[reserve]:  # i遍历到的位置和reserve不同时, 即下一个新元素
                # 找到新的不重复元素，将其放到先前最后一个不重复元素，它就成为新的最后一个不重复元素
                reserve += 1
                nums[reserve] = nums[i]
            i += 1

        # 因为不同于链表，链表是指针指向别的节点，出去上面讲的末尾情况，重复节点是直接被删掉了；而列表是通过交换到最后，所以永远需要切片做截断
        return nums[:reserve + 1]  # 返回结果是个数


if __name__ == "__main__":
    s = Solution()

    nums = [1, 2, 2, 2, 4, 5, 5, 5]

    linked1 = LinkedList(nums)
    print(linked1)
    head1 = linked1.head.next
    print_linked(s.deleteDuplicates(head1))

    print(s.removeDuplicates(nums))
