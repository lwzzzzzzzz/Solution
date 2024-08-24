# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/24 21:15
@Author:     wz
@File:       电话号码的字母组合.py
@Decs:
"""


class Solution:
    def function(self, digits):
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def backtrack(digits, index, path):
            if len(digits) == len(path):
                res.append("".join(path))
                return

            for s in phone_map[digits[index]]:  # 用index代替遍历的digits，对phone_map[digits[index]]做回溯
                path.append(s)
                backtrack(digits, index + 1, path)
                path.pop(-1)

        backtrack(digits, 0, [])
        return res

if __name__ == "__main__":
    s = Solution()
    digits = "23"
    print(s.function(digits))
