class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def reconstructTree(pre_order, mid_order):
    if len(pre_order)==0 or len(mid_order)==0:
        return None
    index = mid_order.index(pre_order[0])
    left = reconstructTree(pre_order[1:index+1], mid_order[:index])
    right = reconstructTree(pre_order[index+1:], mid_order[index+1:])
    return Node(pre_order[0], left, right)

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

    def length(self):
        return len(self.queue)

    def enque(self, val):
        if self.is_full():
            raise Exception('queue is full')
        self.queue.append(val)

    def deque(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self.queue.pop(0)

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
post_order = [7, 4, 2, 5, 8, 6, 3, 1]
tree1 = reconstructTree(pre_order, mid_order)

def level_traversal(tree1):
    q = queue(20)
    q.enque(tree1)
    max_length = 0
    while not q.is_empty():
        if q.length() > max_length:
            max_length = q.length()
        for i in range(q.length()):
            tmp = q.deque()
            if tmp.left:
                q.enque(tmp.left)
            if tmp.right:
                q.enque(tmp.right)

def width(tree1):
    # 求最大树宽度
    q = queue(20)
    q.enque(tree1)
    max_length = 0
    while not q.is_empty():
        if q.length() > max_length:
            max_length = q.length()
        for i in range(q.length()):
            tmp = q.deque()
            if tmp.left:
                q.enque(tmp.left)
            if tmp.right:
                q.enque(tmp.right)
    return max_length

# level_traversal(tree1)
print(width(tree1))