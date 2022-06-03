# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/19 1:20 下午
@Author:     wz
@File:       MinimumWindowSubstring.py
@Decs:
"""

'''

给定两个字符串S 和T，求S 中包含T 所有字符的最短连续子字符串的长度，同时要求时间
复杂度不得超过O(n)


Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

"BANC"包含"ABC"所有字符
'''


class Solution:

    def min_window(self, S, T):
        """
        思路就是：先移动右指针找到符合题意的区间，再移动左指针缩短区间至最短。
            直至右指针到S串的最后，最后再移动一次左指针缩短区间，得到最短子串和其起始索引

            PS：因无顺序要求，判断是否符合题意可以用hashMap去完成
        """

        sub = ""
        start, end = 0, 0
        min_len = len(S) + 1

        need, window = {}, {}
        for s in T:
            try:
                need[s] = need[s] + 1
            except:
                need[s] = 1
                window[s] = 0

        left, right = 0, 0

        # 移动右指针，至满足题意
        while right <= len(S):

            # 当满足题意时，尝试移动左指针缩短长度；如一直未满足题意，sub / start / end等值不会变化
            while self.satisfied(need, window):

                if right - left < min_len:
                    start, end = left, right
                    min_len = end - start
                    sub = S[start: end]

                if window.__contains__(S[left]):
                    window[S[left]] -= 1
                left += 1

            if right < len(S) and window.__contains__(S[right]):
                window[S[right]] += 1
            right += 1

        print("start, end:", start, end)

        return sub

    def satisfied(self, need, window):
        for k, v in need.items():
            if need[k] > window[k]:
                return False
        return True


if __name__ == "__main__":
    S = "ADOBCODEBANBC"
    T = "ABC"

    s = Solution()
    print("最小窗口为: ", s.min_window(S, T))
