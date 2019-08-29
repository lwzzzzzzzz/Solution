
# 整数的二进制表示中有多少个1

def number_of_1(n):
    count = 0
    if n < 0:
        n = ~n + 1
        count += 1
    while n:
        n = n & (n-1)
        count += 1
    print(count)

number_of_1(-4)

# a=-1
# if a & 1: # 效率高于 n % 2
#    print('jishu')