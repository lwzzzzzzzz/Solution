# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/23 3:48 下午
@Author:     wz
@File:       Sqrt.py
@Decs:
"""

'''
为一个非负数开方，并向下取整

input：8
output：2
'''


class Solution:

    def sqrt(self, num):
        """
        二分法可以说是没有难度的算法了，唯一需要注意和规范的点就是，处理边界条件，避免死循环，有两种处理方式（熟练一种基本即可）：
            1、左闭右开（这种符合python /c++的编码习惯）
            2、左闭右闭（这种对边界判断比较直观方便）
            这里说的闭是对应于边界位置会不会被考虑进去，如下代码中
                if (num // mid) < mid:
                    right = mid - 1
                    # right = mid
            mid值已经和num判断过了，此时right = mid - 1，right所指位置显然应该被考虑进去，故为闭区间
                                 而当right = mid，right所指位置已经在if处比较过，不会被取到，故为开区间，对应的while判断条件为left<right，而无需取等号
        Args:
            num:

        Returns:

        """
        if num == 0:
            return num

        left, right = 1, num  # 从1开始，避免mid为0，除数为零

        while left <= right:
            mid = (right - left) // 2 + left  # trick:这里为什么不用(right + left) // 2，因为可能导致int溢出
            if (num // mid) < mid:  # trick:同理这里不用 mid ** 2 > num，也是可能导致int溢出
                right = mid - 1  # 闭区间
            elif (num // mid) > mid:
                left = mid + 1
            else:
                return mid

        return right


if __name__ == "__main__":
    num = 0

    solution = Solution()
    print(solution.sqrt(num))
