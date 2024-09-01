# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/2 0:24
@Author:     wz
@File:       搜索旋转排序数组.py
@Decs:
"""

"""
输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
"""

class Solution:
    def function(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[0] > nums[mid]:
                right = mid - 1
            else:  # 因为题意是不重复的有序数组，实际上走不到这里，只是为了代码完整
                left = mid + 1

        # 旋转点
        # 因为当最后一次进入二分时，left==right都落在旋转点位置，nums[mid]=旋转点值必然小于nums[0]
        # 所以此时right-=1，left不动
        rotate = left
        if target > nums[0]:
            left = 0
            right = rotate - 1
        elif target < nums[0]:
            left = rotate
            right = len(nums) - 1
        else:
            return 0

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    s = Solution()
    print(s.function(nums, target))
