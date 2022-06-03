# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/19 4:27 下午
@Author:     wz
@File:       SumOfSquareNumbers.py
@Decs:
"""

'''
Given a non-negative integer c, your task is to decide whether there’re two integers a and b such that a^2 + b^2 = c.


'''


class Solution:
    def two_square_sum(self, num):

        res = []
        sqrt_num = self.sqrt(num)
        print("sqrt_num: ", sqrt_num)

        right = int(sqrt_num) + (1 if sqrt_num % 1 else 0)
        left = 0
        print("right: ", right)

        while left < right:
            if left ** 2 + right ** 2 == num:
                res.append(left)
                res.append(right)
                break
            elif left ** 2 + right ** 2 > num:
                right -= 1
            elif left ** 2 + right ** 2 < num:
                left += 1

        if res:
            print("v1, v2:", res)
            return True
        else:
            return False

    def sqrt(self, num, p=0.00001):

        left, right = 0, num
        while True:
            mid = (left + right) / 2
            if abs(mid ** 2 - num) < p:
                return mid
            elif mid ** 2 > num:
                right = mid
            elif mid ** 2 < num:
                left = mid


if __name__ == "__main__":
    num = 19
    solution = Solution()
    print(solution.two_square_sum(num))
