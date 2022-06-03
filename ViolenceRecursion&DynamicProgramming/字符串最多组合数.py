# _*_ coding: utf-8 _*_
"""
@Date:       2022/5/1 23:47
@Author:     wz
@File:       字符串最多组合数.py
@Decs:
"""

"""
有一个纯数字组成的字符串，有1-a 2-b ... 26-z的对应关系，给定字符串有多少种对应关系。

input: 1234567
output: 3种 1/2/3/4/5/6/7  12/3/4/5/6/7  1/23/4/5/6/7
"""


class Solution:
    """"
     1、该题有 暴力递归 和 动态规划 两种解法。
    """

    def __init__(self, s):
        self.s = list(map(int, s))

    def combination(self):
        print(self.recursion_combine(0))

    def recursion_combine(self, index):
        """
        当我们在做递归的题目时，一定要学会放弃，学会放弃对整个递归运行栈的思考，要相信数学归纳法的科学性，只考虑当前步的情况，前面步和后续步交给递归过程自己去实现。
        此题思路为：
            1.base case为当前是最后一个元素时，返回1
            2.考虑当前在index位置，因为index之前已经得到其结果，则在index位置，有三种情况：
                1、index位置为0，无法与后面组合或者单独转化为字母，只能和前面的合在一起处理，不存在以0为首的字符串转化，以前面为组合方式的决策是错误的，所以直接返回0。例如：01，可以直接返回0，不需要继续递归；30，递归到0位置，也直接返回0
                2、index位置为1，或者2，后一位为0-6，即可以组合转化为字母，则应该 单独 + 组合 考虑
                3、index位置只能单独考虑的情况，对于当前index位置，只有一种情况，所以最终有多少种情况与后一个位置有关，所以返回self.recursion_combine(index + 1)
        """
        if self.s[index] == 0:  # 此处将等于0的判断放在最前面很关键，因为对于 01 30 120这类的case，优先处理
            return 0

        if index == (len(self.s) - 1):
            return 1

        if self.s[index] == 1 or (self.s[index] == 2 and self.s[index + 1] <= 6):
            if index + 2 <= (len(self.s) - 1):
                # index位置单独处理 + index组合后一位组合处理
                return self.recursion_combine(index + 1) + self.recursion_combine(index + 2)
            else:
                # 当index+2索引越界时，也就是index到了倒数第二个数，则self.recursion_combine(index + 2)可以直接手动+1
                # 为什么不把它考虑进base case呢？ 原因在于，当多出一个还剩2个长度就终止递归情况时，对于120这种case，会出现错误
                return self.recursion_combine(index + 1) + 1
        else:
            return self.recursion_combine(index + 1)


if __name__ == "__main__":
    s = "100"
    s = Solution(s)
    s.combination()
