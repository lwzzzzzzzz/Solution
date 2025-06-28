# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/4 0:15
@Author:     wz
@File:       最长递增子序列.py
@Decs:
"""


class Solution:
    """
        dp[i]的意义表示，当nums[i]被选择后，以该位置为终点的序列，最长递增子序列为多长。
        1. dp[0]第一个元素，显然应该是dp[0]=1
        2. dp[i]时，我们应该遍历在nums[i]之前的更小的元素，选择其最大的，然后 +1 (把nums[i]选上)
        3. 最后返回 max(dp)
    """

    def function(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n  # 每个位置最差也能单独成一个递增子序列

        for i in range(1, n):
            for j in range(i):  # 遍历前面所有元素
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 接在 dp[j] 后面
        print(dp)
        return max(dp)

    def bisect_left(self, a, target):
        left = 0
        right = len(a) - 1
        result = len(a)

        while left <= right:
            mid = (left + right) // 2

            if a[mid] >= target:
                # 可能是一个候选位置，继续向左找更优解
                result = mid
                right = mid - 1
            else:
                # 需要往右找
                left = mid + 1

        return result

    def length_of_LIS(self, nums):
        # tail[i]含义为长度为i+1长度的递增子串，最后结尾的数字，最小数字什么；
        #   如tail[1]，则对于nums = [10, 9, 2, 5, 3, 7, 101, 18]，长度为2的最优递增子串为[2,3]，则tail[1] = 3
        tail = []

        for num in nums:
            # 看看如果把num值塞进tail内，会放在哪个index。位置应该在tail中 >= num的第一个位置
            index = self.bisect_left(tail, num)

            if index == len(tail):
                # num 比所有元素都大，加入 tail
                tail.append(num)
            else:
                # 否则替换掉原来的位置，保持 tail 尽量小
                tail[index] = num

        return len(tail)


if __name__ == "__main__":
    s = Solution()
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.function(nums))
    print(s.length_of_LIS(nums))
