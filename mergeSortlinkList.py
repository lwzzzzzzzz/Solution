# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not l1 and not l2:  # l1和l2链表均不存在
#             return None
#         if not l1:  # l1链表不存在
#             return l2
#         if not l2:  # l2链表不存在
#             return l1
#         while l2:  # 将l2链表中的结点一个一个插入l1链表中
#             l2_temp_node = ListNode(l2.val)  # 将l2中结点赋值为新结点，链表作为参数进行函数传递会随函数进行动态变换
#             l1 = nodeInsert(l1, l2_temp_node)
#             l2 = l2.next
#         return l1
#
#
# def nodeInsert(l1, node):
#     head_node = ListNode(0)  # 头指针
#     head_node.next = l1
#     moder_node = ListNode(0)  # 指向当前结点的前一个结点
#     if node.val < l1.val:  # 结点小于头结点
#         node.next = l1
#         head_node.next = node
#         return head_node.next
#     moder_node = l1  # 链表往后移一位
#     l1 = l1.next
#     while l1:  # 遍历判断链表
#         if l1.val > node.val:  # 判断
#             node.next = l1
#             moder_node.next = node
#             return head_node.next
#         else:  # 往后遍历链表
#             moder_node = l1
#             l1 = l1.next
#     moder_node.next = node  # 结点大于链表中任意结点
#     return head_node.next
#

p1 = ListNode(0)
l1 = p1
p2 = ListNode(0)
l2 = p2
for i in [1,4,5]:
    temp = ListNode(i)
    p1.next = temp
    p1 = p1.next

for i in [1,2,7]:
    temp = ListNode(i)
    p2.next = temp
    p2 = p2.next

# while l1:
#     print(l1.val)
#     l1 = l1.next
# print(l1.next.val)
def merge(l1, l2):
    p3 = ListNode(0)
    l3 = p3
    if not (l1 and l2):
        return l3
    l1, l2 = l1.next, l2.next
    while l1 and l2:
        if l1.val > l2.val:
            p3.next = l2
            l2 = l2.next
        else:
            p3.next = l1
            l1 = l1.next
        # print(p3.val)
        p3 = p3.next
    if l1:
        p3.next = l1
    if l2:
        p3.next = l2
    return l3

res = merge(l1,l2)
while res:
    print(res.val)
    res = res.next
