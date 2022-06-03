# _*_ coding: utf-8 _*_
"""
@Date:       2022/2/13 15:02
@Author:     wz
@File:       对几乎有序的数组排序.py
@Decs:
"""

import heapq

"""
已知一个几乎有序的数组。几乎有序是指，如果把数组排好序的话，每个元素移动的距离一定不超过k，并且k相对于数组长度来说是比较小的。请选择一个合适的排序策略，对这个数组进行排序
"""


class Solution:
    """
    这题因为限定了每个元素移动的距离一定不超过k，所以，可以从下标为0开始依次往后确定元素位置，暴力求解的话，每次需要比较k次，确定当前位置元素。时间复杂度为O(N*k)。
        那么当我们用堆去维护当前位置后的k个元素时，确定当前位置元素 可以从暴力的k次 -> log(k)次，时间复杂度为O(N*log(k))
    """

    def __init__(self, nums, k):
        self.nums = nums
        self.k = k

    def sort(self):
        h = []
        i = 0
        while i <= self.k:
            heapq.heappush(h, self.nums[i])  # 三方包默认是最小堆
            i += 1

        index = 0
        while i <= len(self.nums) - 1:
            self.nums[index] = heapq.heappop(h)
            heapq.heappush(h, self.nums[i])
            index += 1
            i += 1

        while h:
            self.nums[index] = heapq.heappop(h)
            index += 1


if __name__ == "__main__":
    nums = [1, 4, 6, 7, 2, 4, 6, 7, 9, 100]
    s = Solution(nums, 3)
    s.sort()
    print(s.nums)

# h = []
# # for i in range(self.k + 1):
# heapq.heappush(h, 1)
# heapq.heappush(h, 6)
# heapq.heappush(h, 2)
# heapq.heappush(h, 100)
# heapq.heappop(h)
# print(h)
