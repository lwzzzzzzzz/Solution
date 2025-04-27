# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/13 1:01
@Author:     wz
@File:       字符串解码.py
@Decs:
"""

"""
输入：s = "3[a]2[bc]"
输出："aaabcbc"

输入：s = "3[a2[c]]"
输出："accaccacc"
"""

'''
思路，因为"3[a2[c]]"的情况下，我们需要优先处理内部的[]，在处理外部的[]，这种顺序自然想到用栈实现

假设栈内为 【 3,[,a,2,[,c 】，此时]入栈，
我们需要一直往前弹出，直到遇到[，记录当前的字符串'c'和重复次数2；     栈内：【 3,[,a 】
拼接好字符串后，因为仍然需要机选前面的[逻辑，再次入栈。    栈内：【 3,[,a,c,c 】
]再次入栈，栈内元素出栈，记录当前的字符串'acc'和重复次数2，此时把上面的逻辑再次重复一遍；        栈内：【 a,c,c,a,c,c,a,c,c 】
'''


class Solution:
    def function(self, s):
        stk = []
        for ss in s:
            # 不是"]"，照单全收，进栈
            if ss != "]":
                stk.append(ss)
            else:
                # 遇到"]",把"[]"裹起来的单词取出，记为word
                word = ""
                while stk[-1] != "[":
                    word = stk.pop() + word
                # 弹出"["
                stk.pop()

                cnt = int(stk.pop())
                # 因为会有大于10的次数，所以再写一个while，得到次数，如100
                # t = 1
                # while len(stk) > 0 and "0" <= stk[-1] <= "9":
                #     t *= 10
                #     cnt += int(stk.pop()) * t

                # 得到重复的字符串后，继续压入栈
                _s = cnt * word
                print(word)
                # stk.extend(list(_s))
                for _ss in _s:
                   stk.append(_ss)

        return "".join(stk)


if __name__ == "__main__":
    sss = Solution()
    s = "3[a2[c]]"
    print(sss.function(s))
