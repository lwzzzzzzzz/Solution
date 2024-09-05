# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/5 1:21
@Author:     wz
@File:       前K个高频元素.py
@Decs:
"""
import heapq


class Solution:
    """
        用一个map来记录 出现的数字：出现数字的频次；
        再用一个len(nums) + 1长度的数组tmp来记录，tmp[出现数字的频次] = 出现的数字；
        最后从前往后遍历，直到res装满了k个元素为止
    """

    def function(self, nums, k):
        tmp = [[] for _ in range(len(nums) + 1)]
        d1 = dict()
        for i in range(len(nums)):
            if nums[i] in d1.keys():
                d1[nums[i]] = d1[nums[i]] + 1
            else:
                d1[nums[i]] = 1

        for key, value in d1.items():
            tmp[value].append(key)

        res = []
        for i in range(len(tmp) - 1, -1, -1):
            for num in tmp[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return res

    """
        用堆去做这个事情
        用一个map来记录 出现的数字：出现数字的频次；
        然后让map每一个元素入堆中
    """

    def topKFrequent(self, nums, k):
        count = dict()
        for num in nums:
            if num in count.keys():
                count[num] = count[num] + 1
            else:
                count[num] = 1

        # heapq python默认只有对小堆，要用最大堆，需要把原始数组取负号入堆，然后pop后再去负号还原
        heap = []
        for key, val in count.items():
            if len(heap) < k:  # 当堆的大小小于k时，元素入堆
                heapq.heappush(heap, (val, key))  # python中这种情况heapq.heappush(heap, (val, key))堆是按照val排序的
            else:
                if val > heap[0][0]:  # 当堆内元素等于k时，则需要比较堆顶元素和当前元素，如果当前元素大于堆顶元素，那么pop，让前元素入堆
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
        res = []
        for val, key in heap:
            res.append(key)
        return res


if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    xxx = s.function(nums, k)
    print(xxx)

    re = s.topKFrequent(nums, k)
    print(re)
