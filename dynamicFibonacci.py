
# fibonacci: 1 1 2 3 5 ...
res=[1,1] # 保存答案

def fib(n):
    if n==1 or n==2:
        return 1
    is_exist = len(res)>=n
    if is_exist: # 如果有答案则读res
        return res[n - 2] + res[n - 3]
    for i in range(len(res), n): # 没有答案则计算并保存
        res.append(res[i - 1] + res[i - 2])
    return res[-1]


print(fib(5))
print(res)
print(fib(7))
print(res)
print(fib(3))
print(res)