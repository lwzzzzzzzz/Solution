# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/24 0:08
@Author:     wz
@File:       递归构建二叉树.py
@Decs:
"""

from BinaryTree import Node

'''
递归方法构建一棵二叉树
'''

'''
包括 
1. 已知 <前序> <中序> 遍历
2. 已知 <后序> <中序> 遍历
3. 已知 <层序> <中序> 遍历
4. 一种特殊的 <序列化> <反序列化> 
四种情况构建二叉树
'''

class Solution:
    # 4.<序列化> <反序列化> 其实就是把每一个节点的左右孩子（包括左右孩子为空的情况）都字符串化；和把已经字符化了的字符串 解析成一棵真正的树
    def serial_tree_by_pre(self, node):
        if node is None:
            return "#_"

        res = (str(node.value) + "_")
        res += self.serial_tree_by_pre(node.left)
        res += self.serial_tree_by_pre(node.right)
        return res


    # 反序列化
    def deserial_tree_by_pre_str(self, pre_str):
        pre_list = pre_str.strip("_").split("_")
        print(pre_list)


    # 1. 已知 <前序> <中序> 遍历
    # 前序遍历：[根节点, [左子树的前序遍历结果], [右子树的前序遍历结果]]
    # 后序遍历：[[左子树的中序遍历结果], 根节点, [右子树的中序遍历结果]]
    # 所以我们只需要根据前序遍历，找到根节点，再通过后序遍历找到左右子树节点个数，以此递归下去，直到前序遍历结束
    def buildTree(self, preorder, inorder):
        inorder_dict = {}
        for i in range(len(inorder)):
            inorder_dict[inorder[i]] = i

        # 入参含义为 同一个子树在前序遍历和中序遍历下，最左边边界和最右边边界
        def my_tree(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return

            preorder_root = preorder_left  # 前序遍历第一个节点就是root位置
            root = Node(preorder[preorder_root])  # 构建根节点
            inorder_root = inorder_dict[preorder[preorder_root]]  # 根节点在中序遍历中的索引位置
            size_left_subtree = inorder_root - inorder_left  # 从中序遍历中找到左子树的长度

            # preorder_left + 1到preorder_left + size_left_subtree共size_left_subtree个节点，对应左子树先序遍历；
            # 根节点往前的都是中序遍历的节点，对应左子树中序遍历；
            root.left = my_tree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 右子树同理于上面
            root.right = my_tree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        return my_tree(0, n-1, 0, n-1)


if __name__ == "__main__":
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    head.left = n2
    head.right = n3
    n2.left = n4
    n3.right = n5
    n4.left = n6

    s = Solution()
    serial_pre_str = s.serial_tree_by_pre(head)
    print(serial_pre_str)
    s.deserial_tree_by_pre_str(serial_pre_str)

    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    tree_root = s.buildTree(preorder, inorder)
    print(tree_root.left.value)

