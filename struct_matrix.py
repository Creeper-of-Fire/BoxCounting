import math
import numpy





def sphere_make(canvas, r, o_pos):#canvas:画布,r:半径,o_pos:圆心位置
    def distance(p_pos):
        dis_2 = 0
        for i in range(depth_max):
            a = math.fabs(p_pos[i]-o_pos[i])
            dis_2 += a*a
        return math.sqrt(dis_2)
    def is_in_r(p_pos):
        if distance(p_pos) > r:
            return 0
        else:
            return 1
    def recursion(depth, data):
        nonlocal pos_index
        if depth == depth_max:
            if is_in_r(pos_index):
                data = 1
        else:
            for i in range(data[depth]):
                pos_index[depth] = i
                recursion(depth + 1, i)
    n = 0
    box_info = numpy.shape(canvas)
    depth_max = numpy.ndim(o_pos) - 1  # 这里是维数-1
    pos_index = []
    for k in range(depth_max + 1):
        pos_index.append(0)
    for j in range(box_info[0]):
        recursion(0, j)
    return canvas