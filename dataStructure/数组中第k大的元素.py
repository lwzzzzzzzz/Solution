# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/6 1:29
@Author:     wz
@File:       数组中第k大的元素.py
@Decs:
"""
import heapq


class Solution:
    """
        用一个k大小的最小堆存储数据，堆内始终保存的是遍历到目前为止最大的k个数，如果每次遍历到的元素大于堆顶元素，则入堆。
        如果遍历到的元素，甚至不如堆内最小元素，那它必然不是topK大的，因为堆里已经有k个元素了

        O(NlogK)时间复杂度 O(K)空间复杂度
    """
    def function(self, nums, k):
        heap = []
        for i in range(len(nums)):
            if len(heap) < k:  # 当堆的大小小于k时，元素入堆
                heapq.heappush(heap, nums[i])
            else:
                if nums[i] > heap[0]:  # 大于大于堆顶元素
                    heapq.heappop(heap)
                    heapq.heappush(heap, nums[i])

        return heapq.heappop(heap)


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 4, 3]
    k = 2
    xxx = s.function(nums, k)
    print(xxx)

