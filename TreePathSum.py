# 返回树所有路径和为N的路径
import copy

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

pre_order = [1, 2, 4, 7, 6, 3, 5, 6, 8]
mid_order = [4, 7, 2, 6, 1, 5, 3, 8, 6]
root = reconstruct_tree(pre_order, mid_order)

res = []
def path_sum_N(root, sum, N, s):
    if not root:
        return 0
    sum = sum + root.val
    if sum > N:
        return
    s.append(root.val)
    if sum == N and (not root.right and not root.left):
        print(s)
        res.append(copy.deepcopy(s))
    path_sum_N(root.left, sum, N, s)
    path_sum_N(root.right, sum, N, s)
    s.pop()

path_sum_N(root, 0, 9, [])
print(res)
