# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/7 1:23
@Author:     wz
@File:       航班预订统计_差分数组.py
@Decs:
"""


class Solution:
    def corpFlightBookings(self, bookings, n):
        df = [0 for i in range(n)]  # 初始化差分数组
        for first, last, seats in bookings:
            df[first - 1] += seats  # 起始位置应该 +seats
            if last < n:  # 如果航班结束为止不是最后
                df[last] -= seats  # 航班结束位置应该 -seats

        res = [0 for i in range(n)]

        # 经典还原原数组
        res[0] = df[0]
        for i in range(1, n):
            res[i] = res[i - 1] + df[i]
        return res


if __name__ == "__main__":
    s = Solution()
    bookings = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
    n = 5
    print(s.corpFlightBookings(bookings, n))


