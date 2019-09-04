class Stack():
    def __init__(self, size):
        self.size = size
        self.min_val = []
        self.stack = []

    def __str__(self):
        return str(self.stack)

    def is_empty(self):
        if not self.stack:
            return True
        return False

    def is_full(self):
        if len(self.stack) == self.size:
            return True
        return False

    def push(self, val):
        if self.is_full():
            raise Exception('stack is full')
        if self.is_empty():
            self.stack.append(val)
            self.min_val.append(val)
        else:
            self.stack.append(val)
            min_tmp = self.min_val[-1]
            if min_tmp > val:
                self.min_val.append(val)
            else:
                self.min_val.append(min_tmp)

    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')
        self.min_val.pop()
        return self.stack.pop()

    def min(self):
        return self.min_val[-1]

    def length(self):
        return len(self.stack)

stack = Stack(20)
for i in [4,2,3,2,1,5,6]:
    stack.push(i)

nums = stack.length()
while nums:
    print(stack)
    print(stack.min())
    stack.pop()
    nums -= 1