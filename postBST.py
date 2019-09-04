# 判断是否是二叉搜索树的后序遍历
a = [5,8,6,9,11,10,8]

def isPostBST(seq):
    if len(seq)==0:
        # 能到这里的只有一开始seq就是空，因为递归调用前都有if语句
        return False
    root = seq[-1]
    # 找到左右子树的分割索引
    i = 0
    for val in seq[i:-1]:
        if val >= root:
            break
        i += 1
    # 如果右子树有小于root的，则返回False
    for val in seq[i:-1]:
        if val < root:
            return False

    # 这里先设置为True的原因是：针对于左子树或右子树没有或只有一个节点的情况，不需要判断，肯定是true
    left = True
    right = True
    if len(seq[:i])>0:
        left = isPostBST(seq[:i])
    if len(seq[i:-1])>0:
        right = isPostBST(seq[i:-1])
    return left and right

print(isPostBST(a))

