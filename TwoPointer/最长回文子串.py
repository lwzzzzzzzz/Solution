# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/5 0:05
@Author:     wz
@File:       最长回文子串.py
@Decs:
"""


class Solution:

    """
        分为回文子序列为 奇数、偶数 两种情况：
        先确定中心节点方式后，双指针求出以当前节点为中心的最长回文子串，最后比较长度，返回最长。
    """
    def longest_palindrome(self, s: str) -> str:

        max_sub_palindrome = ""
        for i in range(len(s)):
            odd = self.palindrome(s, i, i)  # 以i为中心的奇数长度的回文串
            even = self.palindrome(s, i, i + 1)  # 以i，i+1为中心的奇数长度的回文串

            if len(odd) > len(even):
                i_sub_palindrome = odd
            else:
                i_sub_palindrome = even

            if len(i_sub_palindrome) > len(max_sub_palindrome):
                max_sub_palindrome = i_sub_palindrome
        return max_sub_palindrome

    def palindrome(self, s, left, right):
        # 从中心出发，双指针确定子回文串
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

if __name__ == "__main__":
    so = Solution()
    s = "babad"
    print("最长回文子串：", so.longest_palindrome(s))
