# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/21 4:49 下午
@Author:     wz
@File:       LongestSubstringWithKUniqueCharacters.py
@Decs:
"""

'''
给定一个字符串，找到最多有k个不同字符的最长子字符串。

样例

例如，给定 s = "eceba" , k = 3,
T 是 "eceb"，长度为 4.

O(n), n 是所给字符串的长度
'''


class Solution():
    '''
    有k个不同字符的最长子字符串：很快能想到用hashMap去存储这k个不同的字符，以及它们的个数

    本题是一道典型的双指针维护slide window，即抽象问题为在一个字符串内寻找一个符合要求的连续子串。
    思路为：右指针right往前走，不断往前遍历，遍历过程中，始终对滑动窗口内元素满足题意时做一个判断，是否更新结果；
          而左指针left只在滑动窗口内元素不满足题意时，往前走，以此维护滑动窗口的左右边界移动。
    '''

    def longest_length(self, s, k):
        res = 0
        res_index = []
        window = {}

        left, right = 0, 0
        for i in range(len(s)):

            try:
                window[s[right]] += 1
            except:
                window[s[right]] = 1

            while len(window.keys()) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    window.pop(s[left])
                left += 1

            if len(window.keys()) == k:
                # res = max(right - left + 1, res)
                tmp_length = right - left + 1
                if res < tmp_length:
                    res = tmp_length
                    res_index = [left, right]

            right += 1

        return res


if __name__ == "__main__":
    s = "eceba"
    k = 3

    solution = Solution()
    print(solution.longest_length(s, k))
