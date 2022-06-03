# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/11 0:31
@Author:     wz
@File:       HeapSort2.py
@Decs:
"""

"""
heap的基本属性，
- 用数组存放heap时：当前节点下标为i，其父节点下标为 (i-1) // 2；其左子节点下标为 2*i + 1；其右子节点下标为 2*i + 2
- 判断当前节点下标i是否有子节点的条件为：1、比较 当前节点下标i 与 最后一个节点的父节点下标：i <= (heap_size-1)-1 // 2 
                                    2、或者比较 当前节点左孩子 与 最后一个节点的下标：2*i+1 <= heap_size-1  ps：为啥是左孩子，因为节点如果有子节点，那它至少有左孩子
- 对于heap来说，其核心有1、堆的向上调整（往堆尾插入）2、向下调整（pop堆顶）**牢记**
"""

class Heap:

    def __init__(self, nums):
        self.nums = nums
        self.heap_size = 0

        # # 初始化堆 方法一：从根节点开始，做向上调整，一直到数组末尾，依次加入heap
        # for index in range(len(self.nums)):
        #     self.heap_insert(index)

        # 初始化堆 方法二：默认该数组已经是一个不需要大量调整的二叉树，则只需要对一些节点做向下调整的操作。
        #           即 从最后一个非叶子节点开始做向下调整，一直到根节点。原理就是，当左右子树都是heap时，只需要调整根节点和其左右孩子即可整合出一个更大的heap
        # 方法二比方法一快：本质在于1、向下调整的过程需要选择左右孩子的较大者，如果用向上调整的思路，则需要进行两次
        self.heap_size = len(self.nums)
        index = ((self.heap_size - 1) - 1) // 2
        while index >= 0:
            self.heapify(index)
            index -= 1

    def heap_insert(self, index):
        child, parent = index, (index - 1) // 2
        # 因为默认是往已经是heap的数组末尾插入元素，则 1、当到达根节点时 2、当父节点大于等于子节点时，此时已是heap -> 跳出循环。
        while child > 0 and self.nums[child] > self.nums[parent]:
            self.nums[parent], self.nums[child] = self.nums[child], self.nums[parent]
            child = parent
            parent = (child - 1) // 2
        self.heap_size += 1

        # # 简化版
        # while index > 0 and self.nums[index] > self.nums[(index - 1) // 2]:
        #     self.nums[index], self.nums[(index - 1) // 2] = self.nums[(index - 1) // 2], self.nums[index]
        #     index = (index - 1) // 2

    def push(self, num):
        self.nums.append(num)
        self.heap_insert(self.heap_size)

    def heapify(self, root):  # 可以从任意索引开始，以其为根节点做自上而下的heapify
        parent = root
        while parent <= ((self.heap_size - 1) - 1) // 2:  # 终止条件为该节点无子节点，则不需要进行交换
            max_child, left_child, right_child = parent * 2 + 1, parent * 2 + 1, parent * 2 + 2
            if right_child <= self.heap_size - 1 and self.nums[left_child] < self.nums[right_child]:  # 如存在右孩子且该值大于左孩子值
                max_child = right_child

            # 如孩子节点的最大值大于父节点值，交换；否则以父节点为根节点的二叉树已经是heap
            if self.nums[parent] < self.nums[max_child]:
                self.nums[max_child], self.nums[parent] = self.nums[parent], self.nums[max_child]
                parent = max_child
            else:
                break

    def pop(self, index):
        res = self.nums[index]
        self.nums[index], self.nums[self.heap_size - 1] = self.nums[self.heap_size - 1], self.nums[index]
        self.heap_size -= 1
        self.heapify(index)
        return res

    def heap_sort(self):
        while self.heap_size > 0:
            print("sort pop:", self.pop(0))


if __name__ == "__main__":
    nums = [1, 4, 6, 7, 2, 4, 6, 7, 9, 100]
    h = Heap(nums)
    print(1, h.nums)

    h.push(10900)
    print(h.nums)

    print(h.pop(0))
    print(h.nums)

    print(h.pop(0))
    print(h.nums)

    print(h.pop(0))

    print(h.nums)

    print(h.pop(0))
    print(h.nums)

    h.heap_sort()
    print(h.nums)



