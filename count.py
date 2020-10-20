import numpy
import struct_matrix as sm
import sketch_to_matrix as stm
import math
# 问：为什么不用Java、C++、JavaScript之流？
# 答：现在python拥护者在网络上的声音比较大，所以决定蹭热度。


def count(image, box_info, e):
    def recursion(depth, p):
        nonlocal n
        nonlocal pos_index
        pos_index[depth] = p
        if depth == depth_max:
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
        # print(data)
        if type(data) == numpy.uint8:
            if data >= 1:
                return 1
            else:
                return 0
        else:
            start = index_list[depth]
            for i_data in data[int(start*e): int(start*e + e)]:
                if recursion(i_data, index_list, depth + 1) == 1:
                    return 1
            return 0

    return recursion(image, index_list, 0)


def liner_fitting(data_x, data_y):
    size = len(data_x)
    i = 0
    sum_xy = 0
    sum_y = 0
    sum_x = 0
    sum_sqare_x = 0
    average_x = 0
    average_y = 0
    while i < size:
        sum_xy += data_x[i]*data_y[i]
        sum_y += data_y[i]
        sum_x += data_x[i]
        sum_sqare_x += data_x[i]*data_x[i]
        i += 1
    average_x = sum_x/size
    average_y = sum_y/size
    return_k = (size*sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
    return_b = average_y-average_x*return_k
    return [return_k, return_b]


image = stm.sketch()
x = []
y = []
for e in numpy.arange(1.5,6,0.5):
    info = list(numpy.shape(image))  # 长宽高等
    for i in range(len(info)):
        info[i] = int(info[i] / e)  # 按照边长进行划分，得到长宽高方向的格子数
    print('ε={}'.format(e))
    print('划分后大小：'+str(info))
    ne = count(image, info, e)
    y.append(math.log(ne))
    x.append(math.log(1/e))
    print('N(ε)={}'.format(ne))
    print('log(N(ε))={}'.format(math.log(ne)))
    print('log(1/ε)={}'.format(math.log(1/e)))
    print('dim_box(S)={}'.format(math.log(ne)/math.log(1/e)))

kb = liner_fitting(x,y)
print('k={},b={}'.format(kb[0],kb[1]))
