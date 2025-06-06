# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/21 2:11 下午
@Author:     wz
@File:       LongestWordInDictionaryThroughDeleting.py
@Decs:
"""

'''
给定一个字符串s和一个字符串词典d，找出词典中最长的那个可以通过删除s中的一些字符得到的字符串。
如果有多个可能的结果，返回最长且字典序最小的字符串。如果没有任何可能的结果，就返回空字符串。 

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output: 
"apple"

Input:
s = "abpcplea", d = ["a","b","c"]
Output: 
"a"
'''


class Solution():

    def longest_word_in_dictionary(self, s, d):

        # 先按照字符串长度倒排，再按字符串顺序排序，因为经验上我们认为越长的字符串，越有可能通过删除得到结果，这样越能提前剪枝搜索空间
        d = sorted(d, key=lambda x: (-len(x), x))

        print(d)
        for word in d:
            if self.match(s, word):
                return word

        return ""

    def match(self, s, word):
        """
            判断 word 是否是字符串 s 的 子序列

            双指针分别遍历s / word，当两指针所指相等，两个指针同时加一；否则s指针加一
            最终word指针到字符串尾部，则说明word存在与s中。
        """
        s_pointer = 0
        word_pointer = 0
        while s_pointer < len(s) and word_pointer < len(word):
            if s[s_pointer] == word[word_pointer]:
                word_pointer += 1  # 如果当前字符相等，就让 word_pointer 向后移动一位（表示匹配了一个字符）
            s_pointer += 1
        return word_pointer == len(word)


if __name__ == "__main__":
    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]

    solution = Solution()
    print(solution.longest_word_in_dictionary(s, d))
