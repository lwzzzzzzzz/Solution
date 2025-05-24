# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/13 0:46
@Author:     wz
@File:       最长不重复子串.py
@Decs:
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
            双指针确定不重复的字符串区间，是否重复用set判断
        """

        left, right = 0, 0
        max_str = ""
        window = set()  # 存储当前的不重复子串
        last_find = dict()  # 存储字符最后一次出现位置
        while right < len(s):
            # 当遍历的位置处出现重复时，说明需要移动left指针去遍历新的不重复子串，那left移动到什么位置呢？
            # 自然是上一次重复的位置再后一个，如"eabcad"，遍历到第二个"a"时，自然left要移动到"b"处，同时再移动left的同时，丢弃set内对应元素，即丢弃"ea"
            if s[right] in window:
                while left <= last_find[s[right]]:
                    window.discard(s[left])
                    left += 1
            # 在处理完重复之后，处理当前元素，即将新元素插入集合，并更新当前元素所处位置
            window.add(s[right])
            last_find[s[right]] = right

            # left和right的窗口判断是否需要更新max_str
            if right - left + 1 >= len(max_str):
                max_str = s[left: right + 1]
            right += 1
            print(max_str)
        return len(max_str)


if __name__ == "__main__":
    solu = Solution()
    ss = "abcabcbb"
    solu.lengthOfLongestSubstring(ss)
