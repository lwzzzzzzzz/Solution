# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/12 14:52
@Author:     wz
@File:       有效括号.py
@Decs:
"""

"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

输入：s = "([)]"
输出：false
输入：s = "(]"
输出：false

输入：s = "{[]}"
输出：true
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = []
        tmp = {"]": "[", ")": "(", "}": "{"}

        for each in s:
            if each in tmp.keys():
                if stack1 and tmp[each] == stack1[-1]:
                    stack1.pop()
                else:
                    return False
            else:
                stack1.append(each)

        if stack1:
            return False
        else:
            return True

if __name__ == "__main__":
    s = Solution()
