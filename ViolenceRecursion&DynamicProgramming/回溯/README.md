回溯问题的模板解法
```python
def backtracking(参数):
    ## 如果在这里存放结果，就是回溯所有节点都是结果
    if 终止条件 
        存放结果  # 在这里就是选取某些节点作为结果（一般是叶子节点）
        return
 
    # for i in range(start, len(candidates)) 和 for i in range(0, len(candidates))的区别：
    # 前者对于candidates=[1,2,3]，不可能有[1,2,1] [1,3,2], [1,3,1]这类倒过头去回溯的序列出现；而后者是可以的
    for 选择：本层可选元素（回溯树中孩子节点数量）:
        处理节点  # 一般是入栈
        
        # 而此处同时有两种处理方式dfs(xxx, path, i)和dfs(xxx, path, i+1)表示是否多次遍历当前i索引位置
        backtracking(路径，选择列表)  # 递归
        
        回溯，撤销处理结果  # 一般是出栈

#   example：
#   candidates = [1,2,3]
    for i in range(start, len(candidates)):
    for i in range(0, len(candidates)):  # 允许倒过头去回溯，一般只有全排列才会用到，也就是对元素排列的顺序也有要求。一般需要剪枝
        path.append(candidates[i])
        # 配合range(start, len(candidates)) 这种情况可以重复取[1,1,1] [1,1,2]...等等case
        # 配合for i in range(0, len(candidates)) 不剪枝下，返回的是全排列  ps：当然很少有这种情况
        dfs(t - candidates[i], path, i)  
        
        # 配合range(start, len(candidates)) 这种情况不能重复取只有[1,2,3]，一种情况
        # 配合for i in range(0, len(candidates)) 不剪枝下，返回的是全排列
        dfs(t - candidates[i], path, i + 1)  
        path.pop(-1)
```