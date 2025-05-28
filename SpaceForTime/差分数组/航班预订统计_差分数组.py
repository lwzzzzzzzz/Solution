# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/7 1:23
@Author:     wz
@File:       航班预订统计_差分数组.py
@Decs:
"""


"""
公司有 n 个预订记录，每个预订记录是一个三元组 [first_i, last_i, seats_i]，分别表示：

意味着在从first_i到last_i（包含 first_i 和 last_i）的每个航班上预订了seats_i个座位。
请你返回一个长度为 n 的数组 answer，里面的元素是每个航班预定的座位总数。

input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
output: [10,55,45,25,25]
"""

class Solution:

    """
        我们只需要知道每一站会减少或增加多少人，根据前一站的人数，加减运算得出这一站的人数即可。这于差分数组的定义一致，
        这一站要变动的人数，就是差分数组本身。

        差分数组定义：
        ps: arr[0] = diff[0]
            arr[i] = arr[i - 1] + diff[i]   （i >= 1）
    """
    def corpFlightBookings(self, bookings, n):
        df = [0 for i in range(n)]  # 初始化差分数组
        for first, last, seats in bookings:
            df[first - 1] += seats  # 起始位置应该 +seats
            if last < n:  # 如果第n站在当前预定记录第last站之后，则后续应该把seats位置释放出来
                # ps: 因为res[last+1] = res[last] + df[last]，所以df[last]位置减去seats就行，对第last+1站产生影响
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


