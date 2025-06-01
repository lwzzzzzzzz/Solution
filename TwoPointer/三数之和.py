# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 1:45
@Author:     wz
@File:       三数之和.py
@Decs:
"""


class Solution:
    """
        求出所有解，则需要考虑去重
    """
    def function(self, nums: list[int]):
        nums.sort()
        print(nums)
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 遍历的i和前一个i-1一样，需要去重
                continue

            target = 0 - nums[i]
            left, right = i + 1, len(nums) - 1  # left从i+1开始遍历，避免重复
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[i], nums[right]])
                    # left下一个移动的位置和当前left位置，答案需要去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # right下一个移动的位置和当前right位置，答案需要去重
                    while left < right and nums[left] == nums[right - 1]:
                        right -= 1
                    # 因为要找到所有的解，所以left、right还要继续往中间走
                    left += 1
                    right -= 1
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function([-1, 0, 1, 2, -1, -4])
    print(xxx)