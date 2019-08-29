
# 是否是2的次方
def is_power_of_two(n):
    return n > 0 and not (n & n - 1)


a = bin(-3)
print(a)

a = bin(3)
print(a)

b = bin(-3 & 0xffffffff)
print(b)

c = 0x80000000
print(c)