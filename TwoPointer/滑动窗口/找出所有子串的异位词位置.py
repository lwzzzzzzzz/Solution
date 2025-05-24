# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/22 0:48
@Author:     wz
@File:       找出所有子串的异位词位置.py
@Decs:
"""


class Solution:
    def find_anagrams(self, s: str, p: str):
        res = []
        len_p = len(p)
        len_s = len(s)

        if len_p > len_s:
            return res

        # 统计 p 的字符频率
        window_count = [0] * 26
        p_count = [0] * 26
        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        left = 0
        right = 0
        while right < len_s:
            # 将右指针对应字符加入窗口
            window_count[ord(s[right]) - ord('a')] += 1

            # 如果窗口大小超过 p 的长度，收缩左边界
            while right - left + 1 > len_p:
                window_count[ord(s[left]) - ord('a')] -= 1
                left += 1

            # 当窗口大小正好等于 p 长度时，比较是否匹配
            if window_count == p_count:
                res.append(left)
                print(s[left: left + len_p])

            right += 1

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.find_anagrams("zcfazgz", "za"))
