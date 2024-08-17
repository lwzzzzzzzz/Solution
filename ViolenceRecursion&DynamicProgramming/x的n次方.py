# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/10 22:24
@Author:     wz
@File:       x的n次方.py
@Decs:
"""


class Solution:
    def my_pow(self, x, n):
        if n < 0:
            return 1 / self.my_pow(x, -n)

        if n == 1:
            return x
        if n % 2 == 0:
            return self.my_pow(x, n / 2) * self.my_pow(x, n / 2)
        if n % 2 == 1:
            return x * self.my_pow(x, (n - 1) / 2) * self.my_pow(x, (n - 1) / 2)


if __name__ == "__main__":
    s = Solution()
    print(s.my_pow(3, -5))
