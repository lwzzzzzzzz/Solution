# _*_ coding: utf-8 _*_
"""
@Date:       2024/9/7 17:42
@Author:     wz
@File:       分割回文串.py
@Decs:
"""

"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。返回 s 所有可能的分割方案
"""


class Solution:
    """
        用一个dp数组维护当前字串是不是回文子串，dp[i][j]表示从i到j的字串是否是回文子串，取值为true false
    """

    def function(self, s):
        n = len(s)
        res = []

        dp = [[False] * n for _ in range(n)]
        # dp方法求所有可能组成回文子串的状态
        #   因为dp[i][j]的状态需要比较s[i] s[j]和dp[i+1][j-1]才能得到，可以看到i依赖i+1位置，
        #   我们一般时横着递推，让i从1递推到n，但是这里因为存在依赖，所以不行。但我们可以让j从0开始递推，竖着递推
        for j in range(n):
            for i in range(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif s[i] == s[j]:
                    if j - i <= 2:  # 当子字符串长度为2时，不依赖上一个状态，只要s[i] == s[j]，就符合回文定义
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

        # # 使用中心扩散法填充 dp 数组
        # for mid in range(n):
        #     # 奇数长度回文
        #     left, right = mid, mid
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         dp[left][right] = True
        #         left -= 1
        #         right += 1
        #     # 偶数长度回文
        #     left, right = mid, mid + 1
        #     while left >= 0 and right < n and s[left] == s[right]:
        #         dp[left][right] = True
        #         left -= 1
        #         right += 1
        print(dp)

        def dfs(s, dp, start, path):
            if start == n:  # 当遍历到最后返回path
                res.append(path[:])
                return

            for i in range(start, n):  # 每次从开始位置，因为我们要求的是每个子串的集合，所以可选元素就是从start开始
                if not dp[start][i]:  # 对回溯树进行剪枝，只留下符合要求的子树
                    continue
                path.append(s[start: i + 1])  # 把结果加入path
                dfs(s, dp, i + 1, path)  # i字符符合要求，则加入到path，这时的start就变成i + 1
                path.pop(-1)

        # 在知道了所有的dp位置关系之后，我们可以通过dp位置关系，通过回溯，找到所有的分割回文子串的集合
        dfs(s, dp, 0, [])
        return res


if __name__ == "__main__":
    ss = Solution()
    s = "aab"
    print(ss.function(s))
