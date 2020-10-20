import math
import numpy





def sphere_make(canvas, r, o_pos):  # canvas:画布,r:半径,o_pos:圆心位置
    def distance(p_pos):
        dis_2 = 0
        for i in range(depth_max + 1):
            a = math.fabs(p_pos[i]-o_pos[i])
            dis_2 += a*a
        return math.sqrt(dis_2)

    def is_in_r(p_pos):
        if distance(p_pos) > r:
            return 0
        else:
            return 1
    def recursion(depth, cnvs):
        nonlocal pos_index
        #print(pos_index)
        if depth > depth_max:
            if is_in_r(pos_index):
                return 1
            else:
                return 0
        else:
            data = []
            for i in range(len(cnvs)):
                pos_index[depth] = i
                data.append(recursion(depth + 1, cnvs[i]))
            return data

    n = 0
    box_info = list(numpy.shape(canvas))
    depth_max = len(box_info) - 1  # 这里是维数-1
    pos_index = []
    for k in range(depth_max + 1):
        pos_index.append(0)
    m_print = numpy.array(recursion(0, canvas))
    canvas = numpy.add(canvas,m_print)
    return canvas