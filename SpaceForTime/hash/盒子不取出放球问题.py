# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/8 22:25
@Author:     wz
@File:       盒子不取出放球问题.py
@Decs:
"""

"""
    有N个盒子boxes，每个盒子都有若干个球[N1, N2, N3, ... , Nx]，现不取出德放球，使之两两不想等，问最少需要放入多少个球。
"""


class Solution:
    """
        用一个set去保存现在有的元素，避免了当前元素是否有重复的这次循环。
    """
    def min_ball_cnt(self, boxes):
        m = set()
        res = 0
        m.add(boxes[0])
        for i in range(1, len(boxes)):
            tmp = boxes[i]
            while tmp in m:  # 当前元素set内是否有相同的，有相同的则不停地 +1，直到成为新元素，之后跳出循环，把新元素加到set内
                tmp += 1
                res += 1
            m.add(tmp)

        return res


if __name__ == "__main__":
    boxes = [2, 4, 4, 4, 6]
    s = Solution()
    print(s.min_ball_cnt(boxes))
