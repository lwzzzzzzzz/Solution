# _*_ coding: utf-8 _*_
"""
@Date:       2022/6/7 0:57
@Author:     wz
@File:       每日温度_单调栈.py
@Decs:
"""


"""
题意：给定一组每天的温度[5, 7, 7, 3, 8, 9]，对于所有天数，找到过多少天后温度比当天高（后续没有比当天高的赋值为0）

in: [5, 7, 7, 3, 8, 9]
out: [1, 3, 2, 1, 1, 0]

"""

class Solution:
    """
        本题采用单调栈完成
    """
    def dailyTemperatures(self, temperatures):
        """
            核心思想：通过一次遍历完成 某种前后关系的确定。
                一般来说，确定一个列表内的所有元素的前后关系，需要两个for循环完成，但是这里用空间换时间的方式，
                通过一个栈来存储前面的元素，在遍历后面的时候，用出栈来代替一次for循环为前面元素寻找关系，出栈了的元素即为完成了前后关系的确认，直到遍历完成
        """
        res = [0 for _ in range(len(temperatures))]
        stack1 = []  # 栈内单调递减
        for i in range(len(temperatures)):
            # 当遍历到的元素比栈顶元素大的话，找到了栈顶元素根据题意的结果；同理对于栈内所有元素，当满足下标i位置和栈顶元素满足条件，反复出栈返回结果
            while stack1 and temperatures[stack1[-1]] < temperatures[i]:
                peek = stack1.pop(0)  # 处理栈顶元素，返回栈顶元素下标
                res[peek] = i - peek
            stack1.append(i)  # 下标入栈
        return  res


if __name__ == "__main__":
    temperatures = [5, 7, 7, 3, 8, 9]
    s = Solution()
    print("res: ", s.dailyTemperatures(temperatures))

