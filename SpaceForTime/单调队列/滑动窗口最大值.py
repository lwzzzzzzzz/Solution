# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/23 0:23
@Author:     wz
@File:       滑动窗口最大值.py
@Decs:
"""


class Solution:
    def function(self, nums, k):
        q = []  # 单调队列
        res = []
        for i in range(len(nums)):  # 遍历nums
            # 队列不为空 && 且滑动窗口应该滑动 队首元素需要出队
            while q and i - q[0] + 1 > k:
                q.pop(0)  # 队头抛出

            # 队列不为空 && 且不符合单调的性质 队尾元素需要出队
            # 当nums[q[-1]] > nums[i]时，队尾元素大于当前元素时，出队，维护单调队列严格递增，
            #       则队头元素每次保存位置时滑动窗口的最小值
            # 当nums[q[-1]] < nums[i]时，队尾元素小于当前元素时，出队，维护单调队列严格递减，
            #       说明每次添加新元素的时候，队头元素是滑动串口内最大的，则队头元素每次保存位置时滑动窗口的最大值
            while q and nums[q[-1]] > nums[i]:
                q.pop(-1)  # 队头抛出

            # 加入当前元素
            q.append(i)

            if i + 1 >= k:
                res.append(nums[q[0]])
        return res


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    s = Solution()
    print(s.function(nums, k))
