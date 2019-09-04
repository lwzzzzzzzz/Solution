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

def reconstructTree2(post_order, mid_order):
    if len(post_order)==0 or len(mid_order)==0:
        return None
    index = mid_order.index(post_order[-1])
    left = reconstructTree2(post_order[:index], mid_order[:index])
    right = reconstructTree2(post_order[index:-1], mid_order[index+1:])
    return Node(post_order[-1], left, right)

def traversal(root):
    if not root:
        return
    print(root.val)
    traversal(root.left)
    traversal(root.right)

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
post_order = [7, 4, 2, 5, 8, 6, 3, 1]
tree1 = reconstructTree(pre_order, mid_order)
tree2 = reconstructTree2(post_order, mid_order)
# traversal(tree1)

def image_tree(root):
    # 在树的递归算法中，一般都需要使用树的遍历，考虑是先序 中序 后序
    if not root:
        return
    image_tree(root.left)
    image_tree(root.right)
    root.left, root.right = root.right, root.left
    return root

image = image_tree(tree1)
traversal(image)
