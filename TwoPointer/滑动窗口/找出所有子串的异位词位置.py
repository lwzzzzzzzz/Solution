# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/22 0:48
@Author:     wz
@File:       找出所有子串的异位词位置.py
@Decs:
"""


class Solution:
    def function(self, s: str, p: str) -> list[int]:
        res = []
        if len(s) < len(p):
            return res

        s_len, p_len = len(s), len(p)
        s_count = [0] * 26
        p_count = [0] * 26
        for i in range(p_len):
            s_count[ord(s[i]) - 97] += 1
            p_count[ord(p[i]) - 97] += 1

        if s_count == p_count:  # 先判断是否相等，方便下面进行循环
            res.append(0)

        left, right = 0, len(p) - 1
        while right <= len(s) - 2:
            # 先把当前位置的字符去掉，左侧窗口再往前走
            s_count[ord(s[left]) - 97] -= 1
            left += 1
            # 右侧窗口先往前走，再把当前位置的字符加进来
            right += 1
            s_count[ord(s[right]) - 97] += 1

            if s_count == p_count:
                res.append(left)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.function("zcfazgz", "z"))
