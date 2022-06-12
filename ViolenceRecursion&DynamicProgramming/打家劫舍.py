# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/12 23:07
@Author:     wz
@File:       打家劫舍.py
@Decs:
"""


class Solution:
    def rob(self, nums):
        return self.recursion_rob(nums, len(nums) - 1)

    def recursion_rob(self, nums, i):
        """
            递归做法
        """
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        return max(nums[i] + self.recursion_rob(nums, i - 2),
                   self.recursion_rob(nums, i - 1))

    def dp_rob(self, nums):
        """
            dp o(n)空间复杂度做法
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[len(nums) - 1]

    def dp_rob2(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp1 = nums[0]
        dp2 = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # 优化空间，因为dp公式只用了两个状态，即dp[i-2], dp[i-1] 所以用dp1 dp2分别表示当前元素的dp值和前一元素的dp值
            dp1, dp2 = dp2, max(nums[i] + dp1, dp2)
        return dp2


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4]
    print(s.rob(nums))
    print(s.dp_rob(nums))
    print(s.dp_rob2(nums))
