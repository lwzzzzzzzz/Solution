class queue():
    def __init__(self, size):
        self.size = size
        self.queue = []

    def __str__(self):
        return str(self.queue)

    def is_empty(self):
        if not self.queue:
            return True
        return False

    def is_full(self):
        if len(self.queue) == self.size:
            return True
        return False

    def enque(self, val):
        if self.is_full():
            raise Exception('queue is full')
        self.queue.append(val)

    def deque(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self.queue.pop(0)

q = queue(10)
for i in [1,2,3,4,5,6]:
    q.enque(i)
    print(i)
