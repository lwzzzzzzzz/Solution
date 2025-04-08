# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/2 5:55 下午
@Author:     wz
@File:       NonOverlappingIntervals.py
@Decs:
"""

'''
question:
给定多个区间，计算让这些区间互不重叠所需要移除区间的最少个数。起止相连不算重叠。

Examples:
输入是一个数组，数组由多个长度固定为2的数组组成，表示区间的开始和结尾。输出一个整数，表示需要移除的区间数量。
Input: [[1,2], [2,4], [1,3]]
Output: 1
'''


class Solution:
    def erase_overlap_intervals(self, intervals):

        # 此题刚拿到完全不知道该如何下手 - -
        # 首先要去掉多少个区间，就是问可以留下来的区间是哪些，共多少个
        # 那这个问题实际上是一个时间区间调度问题，大致有两种解决方案：1、动归(万物皆可动归) 2、贪心
        # 主要实现贪心方法：一个原则，选择区间的时候，为之后的区间留下更多的空间，最终达到该次操作的局部最优
        #               思路为，将区间按结束时间升序排好序后，依次遍历排好序的区间，选取可以选择的空间，保证留给之后的区间段最大即可，最终到全局最优解中的一个

        # 按区间终止位置排好序
        intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            # 当下一个区间的起始位置大于上一个区间的结束位置，则两区间不存在重合，直接加入到结果中，且重置区间起始位置
            if intervals[i][0] > end:
                merged_intervals.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                # 两区间存在重合，有两种情况
                # 1. 当下一个区间的右边界大于当前右边界，则更新区间右边界end为下一个区间的右边界
                # 2. 当下一个区间的右边界小于等于当前右边界，则下一个区间被当前区间包含，不需要操作
                # 而左边界是先排过顺了的，所以不需要考虑。综上，就是取两个区间右边界大的就行
                end = max(end, intervals[i][1])

        merged_intervals.append([start, end])  # 把最后一个区间加进去
        return merged_intervals


'''
note:
1、典型的区间问题，无非先排序（根据起始或终止位置升序or降序排序），再贪心迭代即可。
2、特殊的用扫描线 （待学习）
'''

if __name__ == "__main__":
    intervals = [[1, 3], [3, 5], [2, 7], [3, 7], [2, 3], [5, 8], [7, 8]]

    solution = Solution()
    print(solution.erase_overlap_intervals(intervals))
