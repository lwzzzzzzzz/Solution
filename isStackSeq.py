class Stack():
    def __init__(self, size):
        self.size = size
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def top(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.stack[-1]

    def push(self, val):
        if self.is_full():
            raise Exception('stack is full')
        self.stack.append(val)

    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        return self.stack.pop()

    def length(self):
        return len(self.stack)

in_seq = [1,2,3,4,5]
out_seq = [4,5,2,3,1]

def is_stack_seq(in_seq, out_seq):
    '''
    用stack来存储in_seq的入栈顺序，当与出栈顺序的第一个值相同时，将stack和out_seq这个值同时去除，
    如果最后两个同时为空，则返回true
    :param in_seq:
    :param out_seq:
    :return:
    '''
    stack = []
    while out_seq:
        # 当初始时，stack为空，需要有元素进入stack，进入elif；
        # 又因为out_seq和in_seq长度一样，所以之后不存在stack为None，除非stack和out_seq同时为空，此时结果为true
        # 并且将这个放在 elif in_seq: 前的原因是，优先比对stack和out_seq，是否出栈；否则直接全部先入stack(错误)
        if stack and stack[-1] == out_seq[0]:
            stack.pop()
            out_seq.pop(0)
        elif in_seq:
            stack.append(in_seq.pop(0))
        else:
            # 到这里的情况是，in_seq已经按照入栈顺序完全进入stack，
            # 并且stack出栈顺序和out_seq不匹配 (即stack[-1] == out_seq[0])
            return False
        # 跳出循环时，即最后一次在循环体内执行的是 第一条if后，out_seq为空，跳出；而不会到最后的else
    return True

a = is_stack_seq(in_seq, out_seq)
print(a)