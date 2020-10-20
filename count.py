import numpy as npy
import struct_matrix as sm
# 问：为什么不用Java、C++、JavaScript之流？
# 答：现在python拥护者在网络上的声音比较大，所以决定蹭热度。

image = [[0, 0, 2, 0], [3, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]
e = 2  # 边长

info = list(npy.shape(image))  # 长宽高等
for i in range(len(info)):
    info[i] = int(info[i] / e)  # 按照边长进行划分，得到长宽高方向的格子数
print('划分后大小：'+str(info))


def count(image, box_info, e):
    def recursion(depth, p):
        nonlocal n
        nonlocal pos_index
        pos_index[depth] = p
        if depth == depth_max:
            print('计数区间：'+str(pos_index))
            if count_box(image, pos_index, e) >= 1:
                n += 1
        else:
            for i in range(box_info[depth]):
                recursion(depth + 1, i)
    n = 0
    depth_max = len(box_info) - 1  # 这里是维数-1
    pos_index = []
    for k in range(depth_max + 1):
        pos_index.append(0)
    for j in range(box_info[0]):
        recursion(0, j)
    return n


def count_box(image, index_list, e):
    def recursion(data, index_list, depth):  # 递归
        if type(data) == list:
            start = index_list[depth]
            print(data[start*e: start*e + e])
            for i_data in data[start*e: start*e + e]:
                if recursion(i_data, index_list, depth + 1) == 1:
                    return 1
            return 0
        else:
            if data >= 1:
                return 1
            else:
                return 0
    return recursion(image, index_list, 0)


ne = count(image, info, e)
print('N(ε)={}'.format(ne))
