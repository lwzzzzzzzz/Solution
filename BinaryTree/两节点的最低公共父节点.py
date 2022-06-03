# _*_ coding: utf-8 _*_
"""
@Date:       2022/4/18 0:37
@Author:     wz
@File:       两节点的最低公共父节点.py
@Decs:
"""

from BinaryTree import Node


class Solution:
    """
    给定节点O1和O2，找其最低父节点。
    思路：两种思路，一种是 利用一定的空间复杂度，将所有节点的父节点信息存储在字典内，然后再找到O1的父节点链，然后再从O2的父节点链中找到最低的那个；

        另一种是O(1)空间复杂度的方法，其关键性思路则是，我先向我的左节点要最低父节点，再向右节点要最低父节点，然后合并左右子树结果
            给定节点O1和O2无非两种情况 2.1 一个节点是另一个的祖先，不妨假设O1是O2的祖先，则返回O1
                                    2.2  两个节点不互为祖先，则结果需要综合左右子树得到。
            详细过程较复杂，注释在方法体内
    """

    def __init__(self, head):
        self.head = head

    def lowermost_common_ancestor_dict(self, o1, o2):
        """
        方法一：比较简单直接的方法。
        """
        if o1 == head or o2 == head:
            return head
        if o1 == o2:
            return o1

        parent_dict = dict()
        self.parent_info(self.head, parent_dict)
        print(parent_dict)  # 保存了所有节点到其父节点的映射

        ptr = o1
        o1_parent = [ptr]  # 这里把o1放进去，是为了保证o1是o2的祖先节点时，第二个循环能够跳出
        while ptr != self.head:
            o1_parent.append(parent_dict[ptr])  # o1_parent由下至上保存了o1节点、o1的父节点及其祖先节点
            ptr = parent_dict[ptr]
        # print(o1_parent)
        print(list(map(lambda o: o.value, o1_parent)))

        ptr = o2
        while ptr not in o1_parent:
            ptr = parent_dict[ptr]
        return ptr

    def parent_info(self, ptr, parent_dict):
        if ptr is None:
            return

        if ptr.left is not None:
            parent_dict[ptr.left] = ptr
        if ptr.right is not None:
            parent_dict[ptr.right] = ptr

        self.parent_info(ptr.left, parent_dict)
        self.parent_info(ptr.right, parent_dict)

    def lowermost_common_ancestor(self, ptr, o1, o2):
        """
            向左右子树要最低父节点，然后结合当前节点合并
        """
        # 当到达叶子节点，或者找到o1或者o2节点时直接返回
        # 为啥找到o1或者o2节点时直接返回呢？ 因为再往下就没有意义了，不妨假设先遇见了o1，此时有两种情况
        #   一是：o1是o2的祖先，那公共父节点显然直接是o1；
        #   二是：o1和o2在不同的子树上，那么公共父节点显然应该是o1的祖先才有可能是。 -> 综上，不管什么情况，遇见o1了，最后最低父节点的结果都与o1的孩子们无关，所以直接返回o1即可。
        if (ptr is None) or (ptr is o1) or (ptr is o2):
            return ptr

        left_lca = self.lowermost_common_ancestor(ptr.left, o1, o2)
        right_lca = self.lowermost_common_ancestor(ptr.right, o1, o2)

        # 需要判断左右节点返回
        #   1.当左右子树返回都为空时，说明o1和o2不在 以当前节点为根节点的树，故继续返回None
        if left_lca is None and right_lca is None:
            return None
        #   2.当左右子树返回都不为空时，说明左右子树分别为o1和o2存在的子树，则返回当前节点，即最低公共父节点
        if left_lca is not None and right_lca is not None:
            return ptr
        #   3.当左子树不为空、右子树为空时，说明以当前节点为根节点的左子树中o1或者o2至少存在一个，而o1或者o2不存在在以当前节点为根节点的右子树
        if left_lca is not None and right_lca is None:
            return left_lca
        #  4.同3
        if left_lca is None and right_lca is not None:
            return right_lca

        """
        ps:虽不是重点，但是我们可以看到，在先序遍历的位置，我们进行了返回，在得到左右子树的结果后，在后序遍历位置又做了返回；
            仔细想，整个过程确实是应该在刚遇到o1或o2节点时，即先序时，返回该节点；也确实需要在得到左右子树结果后，即后序时，针对左右子树结果的不同，
            分类讨论来返回最终结果。
        有一些题，不区分[先中后]序遍历；
        有一些题，需要拿到左右子树全部信息后做处理，则需要在后序；
        有一些题，只需要拿到左节点的值，就可以大概判断需不需要再遍历右子树，这时候应该放在中序
        还有一些提，如本题，只需要第一次遇见就可以决定是否返回，则时候就可以直接放在先序处。
        """


if __name__ == "__main__":
    head = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    head.right = n2
    head.left = n3
    n2.left = n4
    n3.right = n5
    n4.left = n6
    n4.right = n7

    s = Solution(head)
    print(s.lowermost_common_ancestor_dict(n2, n3).value)
    print(s.lowermost_common_ancestor(head, n2, n3).value)
