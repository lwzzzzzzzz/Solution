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

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
post_order = [7, 4, 2, 5, 8, 6, 3, 1]
tree1 = reconstructTree(pre_order, mid_order)

def depth(root):
    if not root:
        return 0
    return max(depth(root.right) + 1, depth(root.left) + 1)

depth_tree = depth(tree1)
print(depth_tree)
