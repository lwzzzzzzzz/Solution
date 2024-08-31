# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/30 0:36
@Author:     wz
@File:       单词拆分.py
@Decs:
"""


class Solution:
    """
    给你一个字符串 s 和一个字符串列表 wordDict 作为字典。如果可以利用字典中出现的一个或多个单词拼接出 s 则返回 true。
    输入: s = "leetcode", wordDict = ["leet", "code"]
    输出: true
    解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

    输入: s = "applepenapple", wordDict = ["apple", "pen"]
    输出: true
    解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
    """
    def function(self, ss, wordDict):
        """
        dp[i]表示的该ss和wordDict下，从头开始到第i个数长度ss[0:i]的字符串，能不能被wordDict组合而成。
        和完全平方数一样的思路，就是假如dp[j]=true，如果s[j:i+1]存在在wordDict内，那么则dp[j]也为true，最后返回dp[ss.length]
        """
        n = len(ss)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            # 这里的下标可能需要想一下，首先根据dp数组的定义，dp[0]肯定为True，并且肯定要从dp[0]递推，所以j从0开始遍历，range(0, i)正好遍历长度为i的字符串
            # 同时ss[j:i]表示j.j+1.j+2...i-2.i-1的字符串，符合dp数组的定义
            for j in range(0, i):
                if dp[j] and ss[j:i] in wordDict:
                    dp[i] = True
        return dp[len(ss)]


if __name__ == "__main__":
    s = Solution()
    s1 = "applepenapple"
    wordDict = ["apple", "pen"]
    print(s.function(s1, wordDict))
