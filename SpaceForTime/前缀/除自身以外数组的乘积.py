# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 12:19
@Author:     wz
@File:       除自身以外数组的乘积.py
@Decs:
"""
"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。请不要使用除法
输入: nums = [1,2,3,4]
输出: [24,12,8,6]
"""

class Solution:
    """
        用前缀积数组pre_multi[i]来存储前i-1个元素的乘积; 后缀积数组post_multi[i]来存储后i-1个元素的乘积;
        结果就是pre_multi[i] * post_multi[i]
    """
    def function(self, nums):
        n = len(nums)
        pre_multi = [0] * n
        post_multi = [0] * n
        pre_multi[0] = 1
        post_multi[n-1] = 1

        res = []
        for i in range(1, n):
            pre_multi[i] = pre_multi[i - 1] * nums[i-1]
        print(pre_multi)

        for i in range(n - 2, -1, -1):
            post_multi[i] = post_multi[i + 1] * nums[i+1]
        print(post_multi)

        for i in range(n):
            res.append(pre_multi[i] * post_multi[i])
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function([1, 1, 2, 12])
    print(xxx)
