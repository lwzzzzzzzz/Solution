# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 0:48
@Author:     wz
@File:       最长连续序列.py
@Decs:
"""

'''
示例 1：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

示例 2：
输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
'''


class Solution:
    def function(self, nums: list[int]):
        st = set(nums)
        res = 0
        for i in st:
            if i - 1 not in st:  # 当i-1不在集合中，说明i为连续序列的开头
                num = i
                while num in st:  # 往后连续数字遍历，在st内则长度+1
                    num = num + 1
                res = max(res, num - i)  # 最终这次连续长度为：num - i
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.function([1, 2, 3, 3]))
