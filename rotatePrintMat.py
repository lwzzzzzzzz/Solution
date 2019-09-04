# 顺时针打印矩阵
# 可以考虑每次pop第一行，后逆时针旋转矩阵，再打印第一行，直到矩阵为空
#      1,2,3   pop          rotate  6,9
#      4,5,6  ---->  4,5,6  ----->  5,8  ....
#      7,8,9         7,8,9          4,7
# 结果为123 69 87 ...
# 问题变成怎么旋转矩阵 观察旋转后的数字对应旋转前的下标         rotate  6 [0,2],9 [1,2]
#                                                        4,5,6  ----->  5 [0,1],8 [1,1]  ....
#                                                        7,8,9          4 [0,0],7 [1,0]
#          可以看出用两个循环即可，外层为[i,j] j位置，内层为i位置
a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

# 翻译 row：行 col：列
def rotate(mat):
    row = len(mat)
    col = len(mat[0])
    new_mat = []
    for i in range(col - 1, -1, -1):
        each_mat_line = []
        for j in range(row):
            each_mat_line.append(mat[j][i])
        new_mat.append(each_mat_line)
    return new_mat

def print_mat(mat):
    res = []
    while mat:
        res.extend(mat.pop(0))
        if not mat:
            break
        mat = rotate(mat)
    print(res)

print_mat(a)
# a = list(zip(*a)) # 实现转置
