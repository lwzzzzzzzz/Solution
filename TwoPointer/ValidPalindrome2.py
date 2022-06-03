# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/20 12:46 上午
@Author:     wz
@File:       ValidPalindrome2.py
@Decs:
"""

'''
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
'''


class Solution():
    """
    思路：判断首尾是否相同，如相同则判断中间子串是否满足题意；如不同判断删除首部或尾部后，剩下是否为回文子串
    1、双指针
    2、显然符合递归的思路
    """

    def is_palindrome(self, s):

        # 判断s[left: right+1]子串是否为回文子串
        def check_palindrome(left, right):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(s) - 1
        while left <= right:

            # 如果起始等于结束，则判断剩下的子串是否符合题意
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # 依照题意，可删除一次，即判断删除left位置 / 或right位置后，剩下是否为回文子串
                return check_palindrome(left + 1, right) or check_palindrome(left, right - 1)

        return True

    def recursive_is_palindrome(self, s, left, right, chance):

        if left > right:
            return True

        if s[left] == s[right]:
            return self.recursive_is_palindrome(s, left + 1, right - 1, chance)
        else:
            if chance == 0:
                return False
            else:
                return self.recursive_is_palindrome(s, left, right - 1, chance - 1) \
                       or self.recursive_is_palindrome(s, left + 1, right, chance - 1)


if __name__ == "__main__":
    s = "abca"
    solution = Solution()
    print(solution.is_palindrome(s))
    print(solution.recursive_is_palindrome(s, 0, len(s) - 1, 1))
