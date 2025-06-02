回溯问题的模板解法
```python
def backtracking(参数):
    ## 如果在这里存放结果，就是回溯所有节点都是结果
    if 终止条件 
        存放结果  # 在这里就是选取某些节点作为结果（一般是叶子节点）
        return
 
    # 可以选择是否每次都从头选择元素
    for 选择：本层可选元素（回溯树中孩子节点数量）:
        是否剪枝
        
        处理节点  # 一般是入栈
        
        # 而此处同时有两种处理方式dfs(xxx, path, i)和dfs(xxx, path, i+1)表示是否多次选择当前元素
        backtracking(路径，选择列表)  # 递归进入下一决策树
        
        回溯，撤销处理结果  # 一般是出栈

        
#   example：
def backtrack(start, path):
    res.append(path[:])
    candidates = [1,2,3]
    # 标准子集生成（无重复元素）
    # res结果为：[[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]
    for i in range(start, len(candidates)):
        path.append(nums[i])
        backtrack(i + 1, path)  # 下一层从 i+1 开始
        path.pop()
    
    # 允许重复选当前元素
    # 未剪枝前res结果为：[[], [1], [1,1], [1,1,1],..., [1,2], [1,2,2], ...]
    for i in range(start, len(nums)):
        if condition:  # 通常需要剪枝，否则无限递归
            continue
        path.append(nums[i])
        backtrack(i, path)  # 下一层仍从 i 开始
        path.pop()
    
    # 每次从头开始遍历（允许任意顺序）
    # 未剪枝前len(res)==len(candidates)时，res结果为：[[1,1,1], [1,1,2], [1,1,3], [1,2,1], [1,2,2], [1,2,3], [3,2,1]...]
    for i in range(0, len(nums)):  # 允许倒过头去回溯，一般只有全排列才会用到，也就是对元素排列的顺序也有要求。一般需要剪枝
        if condition:  # 通常需要剪枝，否则无限递归  ps: 条件为if nums[i] in path:时，返回结果则为全排列
            continue
        path.append(nums[i])
        backtrack(i + 1, path)  # 或者 backtrack(i, path) 理论上结果没区别，因为i都没使用到，但是i+1避免选择重复元素
        path.pop()
```