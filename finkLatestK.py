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

def findK(l1, k):
    p1, travseral = l1.next, l1.next
    while k and travseral:
        print(travseral.val)
        travseral = travseral.next
        k -= 1
    if (not travseral) and (k>0):
        return None
    while travseral:
        travseral = travseral.next
        p1 = p1.next
    return p1.val

print(findK(l1, 5))