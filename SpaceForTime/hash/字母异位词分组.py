# _*_ coding: utf-8 _*_
"""
@Date:       2024/8/21 0:38
@Author:     wz
@File:       字母异位词分组.py
@Decs:
"""
'''
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

示例 2:
输入: strs = [""]
输出: [[""]]

示例 3:
输入: strs = ["a"]
输出: [["a"]]
'''

class Solution:
    def function(self, strs):
        tmp = dict()
        for each_s in strs:
            char_s = list(each_s)
            char_s.sort()
            concat_s = ''.join(char_s)
            if concat_s in tmp.keys():
                t = tmp[concat_s]
                t.append(each_s)
                tmp[concat_s] = t
            else:
                tmp[concat_s] = [each_s]

        res = []
        for each in tmp.keys():
            res.append(tmp[each])
        return res


if __name__ == "__main__":
    s = Solution()
    xxx = s.function(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(xxx)
