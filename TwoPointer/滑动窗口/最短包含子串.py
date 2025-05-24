# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/19 1:20 下午
@Author:     wz
@File:       最短包含子串.py
@Decs:
"""

'''

给定两个字符串S和T，求S中包含T所有字符的最短连续子字符串的长度，并给出子串，同时要求时间复杂度不得超过O(n)


Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

"BANC"包含"ABC"所有字符
'''


class Solution:

    def min_window(self, S, T):
        """
        思路就是：双指针窗口
            1. 初始化两个map（通过map判断当前窗口内的子串是否满足题意）
            2. 先移动右指针找到符合题意的区间
            3. 再尝试移动左指针缩短区间至最短
            直至右指针到S串的最后，最后再移动一次左指针缩短区间，得到最短子串和其起始索引

            PS：因无顺序要求，判断是否符合题意可以用hashMap去完成
        """

        sub = ""
        start, end = 0, 0
        min_len = len(S) + 1

        need, window = {}, {}
        for t in T:
            if t in need:
                need[t] = need[t] + 1
            else:
                need[t] = 1
                window[t] = 0

        left, right = 0, 0

        # 移动右指针，至满足题意
        while right < len(S):

            if S[right] in window:
                window[S[right]] += 1

            # 当满足题意时，尝试移动左指针缩短长度；如一直未满足题意，sub / start / end等值不会变化
            while self.satisfied(need, window):
                if right - left + 1 < min_len:  # 如果当前窗口更短，更新最短子串
                    sub = S[left: right + 1]
                    # start = left  // 如果需要返回下标
                    # end = right + 1

                if S[left] in window:  # 左指针字符在 T 中，减少计数
                    window[S[left]] -= 1
                left += 1

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
