class Node():
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def reconstruct_tree(pre_order, mid_order):
    if len(pre_order)==0 or len(mid_order)==0:
        return None
    index = mid_order.index(pre_order[0])
    left = reconstruct_tree(pre_order[1:index+1], mid_order[0:index])
    right = reconstruct_tree(pre_order[index+1:], mid_order[index+1:])
    return Node(pre_order[0], left, right)

pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
root = reconstruct_tree(pre_order, mid_order)
sub_pre_order = [3,5,6,8]
sub_mid_order = [5,3,8,6]
sub_root = reconstruct_tree(sub_pre_order, sub_mid_order)

def is_sub_tree(cut_root, cut_sub_root):
    # 检查结构
    # 两个if不可替换，因为替换后，当找到子树时，root的值必然也是None，所以应该先检查sub_root
    if not cut_sub_root:
        return True
    if not cut_root:
        return False
    # 检查数值
    if cut_root.val != cut_sub_root.val:
        return False
    # 其实就是同时遍历cut_root树和cut_sub_root树，对其结构和数值一一对比
    return is_sub_tree(cut_root.left, cut_sub_root.left) or is_sub_tree(cut_root.right, cut_sub_root.right)

def have_sub_tree(root, sub_root):
    # 当任何一个是空树时 -> false
    if not root or not sub_root:
        return False
    res = False
    if root.val == sub_root.val:
        # 当当前根节点的值相同时，检查剩下的子节点
        res = is_sub_tree(root, sub_root)
    if not res:
        # 其实就是前序遍历root树并且每一个节点上对比sub_root树，直到找到可能是根节点的节点，跳转到上面if
        res = have_sub_tree(root.left, sub_root) or have_sub_tree(root.right, sub_root)
    return res

a = have_sub_tree(root, sub_root)
print(a)