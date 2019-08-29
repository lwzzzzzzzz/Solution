# 一次跳1格或2格  fibonacci

res=[1,1] # 保存答案

def normalFlog(n):
    if n==1 or n==2:
        return 1
    is_exist = len(res)>=n
    if is_exist: # 如果有答案则读res
        return res[n - 2] + res[n - 3]
    for i in range(len(res), n): # 没有答案则计算并保存
        res.append(res[i - 1] + res[i - 2])
    return res[-1]

# n级台阶，一次可以跳1 2 3 4...n格
# 可以推出为等比数列
crazy_res = []
def crazyFlog(n):
    if n==0 or n==1:
        return 1
    return 2**(n-1)