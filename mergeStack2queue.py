

'''
有两个栈stackA、stackB，A是入栈的，B是出栈的，入栈时，直接进入A即可，出栈时，先判断是否有元素，
如果B没有元素，pop肯定报错，应该先将A中所有的元素压倒B里面，再pop最上面一个元素，如果B中有就直接pop出，就可以，
这是最优的思路，两个栈实现了先进后出，在一起又实现了队列的先进先出。
'''

class Queue():
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        # write code here
        self.stackA.append(node)

    def pop(self):
        # return xx
        if self.stackB: # b栈不空
            return self.stackB.pop()
        elif not self.stackA: # a/b 栈都为空，栈空
            return None
        else:
            while self.stackA: # 将a栈所有值都push至 b栈
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

    def getB(self):
        print(self.stackB)

if __name__ == '__main__':
    alist = [4,5,6,7,8,9,0]
    q = Queue()
    for i in alist[:4]:
        q.push(i)
    print(q.pop(), end=' ')
    q.getB()
    for i in alist[4:]:
        q.push(i)



