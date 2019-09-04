# 根据前序(后序)和中序序列构造树

class Node():
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def reconstruct_tree(pre_order, mid_order):
    if len(pre_order)==0 or len(mid_order)==0:
        return None
    index = mid_order.index(pre_order[0])
    left = reconstruct_tree(pre_order[1:index + 1], mid_order[:index])
    right = reconstruct_tree(pre_order[1 + index:], mid_order[1 + index:])
    return Node(pre_order[0], left, right)

post_traversal = []
pre_traversal = []

def traversalTree(root):
    if not root:
        return
    pre_traversal.append(root.data)
    traversalTree(root.left)
    traversalTree(root.right)
    post_traversal.append(root.data)

if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    root = reconstruct_tree(pre_order, mid_order)