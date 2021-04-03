# 本实验涉及到两种点，一个是基站的点根据论文取值分别为4，40，400个
# 第二种是用户的点取值是4000，40000，400000个
# 因为全部都是均因分布，所以决定以点数的开方的值作为从x，y轴获得数据的数量，
# 比如：
# 4 = 2 x 2
# 40 = 6 x 6 + 4(x,y轴取各6个数，剩下四个数随机分布(下面情况类似))
# 400 = 20 x 20
# 4000 = 63 x 63 + 31
# 40000 = 200 x 200
# 400000 = 632 x 632 + 576
from setting import Settings
import numpy as np

setts = Settings()


class XY:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def BaseStation_is_4():
    x_list = np.linspace(1, setts.map_Xrange, 4)
    y_list = np.linspace(1, setts.map_Yrange, 4)
    four_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            four_list.append(xy)

    return four_list


def BaseStation_is_40():
    x_list = np.linspace(1, setts.map_Xrange, 8)
    y_list = np.linspace(1, setts.map_Yrange, 8)
    fourty_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            fourty_list.append(xy)

    for k in range(4):
        xy = XY(np.random.uniform(1, setts.map_Xrange), np.random.uniform(1, setts.map_Yrange))
        fourty_list.append(xy)
    return fourty_list


def BaseStation_is_400():
    x_list = np.linspace(1, setts.map_Xrange, 22)
    y_list = np.linspace(1, setts.map_Yrange, 22)
    fourHundred_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            fourHundred_list.append(xy)

    return fourHundred_list


def UserPoint_is_4000():
    x_list = np.linspace(1, setts.map_Xrange, 65)
    y_list = np.linspace(1, setts.map_Yrange, 65)
    fourThousand_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            fourThousand_list.append(xy)

    for k in range(31):
        xy = XY(np.random.uniform(1, setts.map_Xrange), np.random.uniform(1, setts.map_Yrange))
        fourThousand_list.append(xy)
    return fourThousand_list


def UserPoint_is_40000():
    x_list = np.linspace(1, setts.map_Xrange, 202)
    y_list = np.linspace(1, setts.map_Yrange, 202)
    fourtyThousand_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            fourtyThousand_list.append(xy)

    return fourtyThousand_list


def UserPoint_is_400000():
    x_list = np.linspace(1, setts.map_Xrange, 634)
    y_list = np.linspace(1, setts.map_Yrange, 634)
    fourHundredThousand_list = []
    for i in range(1, len(x_list) - 1):
        for j in range(1, len(y_list) - 1):
            xy = XY(x_list[i], y_list[j])
            fourHundredThousand_list.append(xy)

    for k in range(576):
        xy = XY(np.random.uniform(1, setts.map_Xrange), np.random.uniform(1, setts.map_Yrange))
        fourHundredThousand_list.append(xy)
    return fourHundredThousand_list


