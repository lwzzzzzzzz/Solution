# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/12 19:25
@Author:     wz
@File:       找出数组中出现次数大于一半的众数.py
@Decs:
"""

"""
给定一个大小为 n 的数组nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于⌊ n/2 ⌋的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1：
输入：nums = [3,2,3]
输出：3

示例 2：
输入：nums = [2,2,1,1,1,2,2]
输出：2
"""


class Solution:
    def majorityElement(self, nums):
        """
            O(N)时间复杂度 O(1)空间复杂度
            思路：遍历数组，出现次数大于一半的记为1，其他-1，最后加和必定大于0，且此时返回的指示元素就是众数。
        """
        # 初始化计数和指示元素
        cnt = 1
        pre = nums[0]

        for i in range(1, len(nums)):  # 从第二个数开始计数
            if pre == nums[i]:  # 当遍历位置数字等于指示元素时，计数 +1
                cnt += 1
            else:
                cnt -= 1  # 当遍历位置数字不等于指示元素时，先 -1，之后看计数是否小于0
                # 当小于0说明当前的指示元素不是已经遍历过部分的众数，此时重新初始化指示元素为当前元素，并置cnt为1
                if cnt < 0:
                    pre = nums[i]
                    cnt = 1
        return pre

    def majorityElement2(self, nums):
        return self.mergeMajorityElement(nums, 0, len(nums) - 1)

    def mergeMajorityElement(self, nums, left, right):
        if right <= left:
            return nums[left]

        # 左右两侧的众数，必然有一个是答案。则可以归并思想处理
        mid = (right - left) // 2 + left
        left_majority_e = self.mergeMajorityElement(nums, left, mid)
        right_majority_e = self.mergeMajorityElement(nums, mid + 1, right)

        if left_majority_e == right_majority_e:  # 如果左右一样，随意返回
            return left_majority_e

        count_left, count_right = 0, 0  # 否则统计nums[left,right + 1]之间的众数是取左边还是右边
        for i in range(left, right + 1):
            if nums[i] == left_majority_e:
                count_left += 1
            if nums[i] == right_majority_e:
                count_right += 1
        if count_left >= count_right:
            return left_majority_e
        else:
            return right_majority_e


if __name__ == "__main__":
    s = Solution()
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(s.majorityElement(nums))
    print(s.majorityElement2(nums))
