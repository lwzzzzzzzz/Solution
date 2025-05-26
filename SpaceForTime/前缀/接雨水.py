# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/22 0:14
@Author:     wz
@File:       接雨水.py
@Decs:
"""


class Solution:
    """
        思路：站在i位置，往左边看，往右边看，能接住水的取决于更短的长度。这里就要用前缀数组和后缀数组来存储i位置往前、往后的最大长度
            使用前缀最大值来保存每一个位置的左边界；用后缀最大值保存每一个位置的有边界。
            此时该位置能接水的容积最大为 1*高度 - 该位置块本身高度。再把所有位置的和加起来就是结果。
    """
    def function(self, height: list[int]) -> int:
        n = len(height)
        pre_max = [0] * n
        pre_max[0] = height[0]  # 前缀最大值数组
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        post_max = [0] * n
        post_max[-1] = height[-1]  # 后缀最最大值数组
        for i in range(n - 2, -1, -1):
            post_max[i] = max(post_max[i + 1], height[i])

        res = 0
        for h, pre, post in zip(height, pre_max, post_max):
            res = min(pre, post) - h + res  # 1*高度 - 该位置块本身高度
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function([0, 1, 3,1,1, 2, 12])
    print(xxx)
