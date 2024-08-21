# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 0:12
@Author:     wz
@File:       tes.py
@Decs:
"""
import collections


class Solution:
    def function(self, s: str) -> int:
        res = 0
        left, right = 0, 0

        set1 = set()
        m1 = dict()
        for right in range(len(s)):
            if s[right] in set1:
                while left <= m1[s[right]]:
                    left += 1
            set1.add(s[right])
            m1[s[right]] = right

            res = max(res, right - left + 1)

        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function("abcc")
    print(xxx)
