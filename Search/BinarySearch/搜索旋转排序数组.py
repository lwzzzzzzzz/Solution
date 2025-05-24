# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/2 0:24
@Author:     wz
@File:       搜索旋转排序数组.py
@Decs:
"""

"""
输入：nums = [4,5,6,0,1,2], target = 0
输出：3
"""

class Solution:
    def function(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:  # 始终与最右边的right位置比较
                left = mid + 1
            elif nums[right] > nums[mid]:
                # 如果right = mid + 1的话，会跳过mid位置的搜索，因为在二分的时候，我们并没有想最正常的二分，给定了确定的target值，
                # 而是用相对关系表示的二分搜索区间，一直用nums[right]作为target。ps：如果是不是左闭右闭的搜索区间的话，就会方便很多
                right = mid
            else:
                # 这里因为取等号的时候，肯定是left和right都在最小值的位置，随便挪动left或right都可以跳出循环
                # 而当挪动了left，最后right就是最小值位置；反之就是left是最小值位置
                left = mid + 1
        print("left:", nums[left], " right:", nums[right])

        # 旋转点
        # 因为当最后一次进入二分时，left==right都落在旋转点位置，nums[mid]=旋转点值时，挪动了left使之跳出循环，所以此时旋转点为right位置
        rotate = right
        if target > nums[-1]:  # 当目标值大于最后一个元素，则目标值在前半段递增区间内
            left = 0
            right = rotate - 1
        elif target < nums[-1]:  # 当目标值小于最后一个元素，则目标值在后半段递增区间内
            left = rotate
            right = len(nums) - 1
        else:
            return len(nums) - 1

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
    target = 5
    s = Solution()
    print(s.function(nums, target))
