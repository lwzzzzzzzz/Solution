- 滑动窗口最值单调队列模版
``` python
n = len(nums)
q = collections.deque()  # 单调队列
for i in range(len(nums)):  # 遍历nums
    while q and checkWindow(i, q[0]):  # 队列不为空 && 且在滑动窗口应该更新
        q.pop(0)  # 队头抛出
    
    while q and check(i, q[-1]):  # 队列不为空 && 且不符合递增的性质元素
        q.pop(-1)  # 队头抛出

    # 加入当前元素
    q.append(i)
```