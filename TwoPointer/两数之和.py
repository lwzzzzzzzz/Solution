# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/5 0:29
@Author:     wz
@File:       两数之和.py
@Decs:
"""


class Solution:
    def twoSum(self, numbers, target):

        """
            对撞指针做法 比较简单
        """
        # left, right = 0, len(numbers) - 1
        # while right > left:
        #     if numbers[left] + numbers[right] > target:
        #         right -= 1
        #     elif numbers[left] + numbers[right] < target:
        #         left += 1
        #     else:
        #         return [left + 1, right + 1]

        # return[-1, -1]

        """
            字典存储已经遍历过的数字，用o(n)的空间换时间。
        """
        d = dict()  # 结构为 {值：下标}
        for i in range(len(numbers)):
            if target - numbers[i] in d.keys():  # 当遍历到i位置时，且target - numbers[i]值也存在于字典中，说明已经满足题意，返回
                return [d[target - numbers[i]] + 1, i + 1]  # 返回时记得先返回字典里已有的，因为数组有序，已有说明值更小
            else:
                d[numbers[i]] = i

if __name__ == "__main__":
    s = Solution()
    numbers = [1, 2, 2, 2]
    target = 4
    print("res: ", s.twoSum(numbers, target))
