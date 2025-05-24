# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/6 1:44
@Author:     wz
@File:       轮转数组.py
@Decs:
"""

"""
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

"""

class Solution:
    def function(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        """
        题解：先翻转整个数组0:len(nums)-1；再翻转0:k-1；最后翻转k:len(nums)-1
             // 唯一要注意的是，当k大于len(nums)，则取k = k % len(nums)
        [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1] -> [5,6,7,4,3,2,1] -> [5,6,7,1,2,3,4] 
        """
        k = k % len(nums)  # k大于len(nums)
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
        return nums


if __name__ == "__main__":
    s = Solution()
    nums = [4, 1, 2, 1, 2]
    print(s.function(nums, 3))
