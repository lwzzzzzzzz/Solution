# 反转链表

class LinkNode():
    def __init__(self, val=0):
        self.val = val
        self.next = None

def creat_link_list(input_linkList):
    l1 = LinkNode(0)
    p1 = l1
    for i in input_linkList:
        tmp = LinkNode(i)
        p1.next = tmp
        p1 = p1.next
    return l1

a = [1,3,4,9,11]
l1 = creat_link_list(a)
# while l1:
#     print(l1.val)
#     l1 = l1.next
def reverse(l1):
    head = l1.next
    if (not head) or (not head.next):
        return l1
    pre = None
    cur = head
    # post保存当前节点的next；cur表示当前节点；pre表示之前节点
    # 先将cur.next赋值为pre；post保存下一个节点的地址；pre cur post先后往前走一格。
    while cur:
        post = cur.next
        cur.next = pre
        pre = cur
        cur = post
    head = LinkNode(0)
    head.next = pre
    return head

def recurReverse(pHead):
    if not pHead or not pHead.next: # not pHead为了防止空链表的情况
        return pHead
    else:
        # 递归从本质上讲，是一个循环，以此处为例，递归到栈底后，返回的newHead一直被传递回来了
        newHead = recurReverse(pHead.next)
        pHead.next.next = pHead
        pHead.next = None
        return newHead

# p1 = reverse(l1)
# while(p1):
#     # print(p1.val)
#     p1 = p1.next

p1 = recurReverse(l1.next)
while(p1):
    print(p1.val)
    p1 = p1.next