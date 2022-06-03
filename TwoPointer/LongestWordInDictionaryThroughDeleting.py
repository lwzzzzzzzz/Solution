# _*_ coding: utf-8 _*_
"""
@Date:       2021/5/21 2:11 下午
@Author:     wz
@File:       LongestWordInDictionaryThroughDeleting.py
@Decs:
"""



'''
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. 
If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

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

        # 先按照字符串长度倒排，再按字符串顺序排序，这样在遍历排序后的list后，第一个满足要求的就一定是符合题意的
        d = sorted(d, key=lambda x:(-len(x), x))

        print(d)
        for word in d:
            if self.match(s, word):
                return word

        return ""


    def match(self, s, word):
        '''
        双指针分别遍历s / word，当两指针所指相等，两个指针同时加一；否则s指针加一
        最终word指针到字符串尾部，则说明word存在与s中。
        Args:
            s:
            word:

        Returns:

        '''
        s_pointer = 0
        word_pointer = 0
        while s_pointer<len(s) and word_pointer<len(word):
            if s[s_pointer] == word[word_pointer]:
                word_pointer += 1
            s_pointer += 1
        return word_pointer == len(word)



if __name__ == "__main__":

    s = "abpcplea"
    d = ["ale", "apple", "monkey", "plea"]

    solution = Solution()
    print(solution.longest_word_in_dictionary(s, d))

