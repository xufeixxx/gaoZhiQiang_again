import random
from util import minDistance
from object.U_Point import UserPoint
import numpy as np
from object import distance
from map import MyMap
import datetime
from util.EM import EM_densityEstimation
import matplotlib.pyplot as plt
import numpy as np
from util.DirectStatistics import DirectEstimate

from util.randomResponse import computeIRR, computePRR

# listkk = []
# for i in range(40):
#     dis = distance.DistanceBetweenTwoPoint(random.randint(1, 50), 1, i + 1)
#     listkk.append(dis)
#
# # for i in range(40):
# #     print(listkk[i].UP_id, "到", listkk[i].BS_id, "的距离是：", listkk[i].dis)
#
# minDistance.quick_sort(listkk, 0, len(listkk)-1)
#
# for i in range(40):
#     print(listkk[i].UP_id, "到", listkk[i].BS_id, "的距离是：", listkk[i].dis)
#
# print("到最近的基站的ID是", listkk[0].BS_id)
#
# print(minDistance.computeMinDistance_BS_ID(listkk))
start_time = datetime.datetime.now()
myMap = MyMap()

myMap.generateUsersPoint()
myMap.generateBaseStationPoint()
myMap.userPoint_set_A()
myMap.userPoint_set_R()
myMap.userPoint_set_U()
# de = DirectEstimate(myMap)
# real_density = de.realDensity()
# estimate_density = de.DirectStatistics_densityEstimation()
# print("用户点的个数是：", myMap.userNum, "\n",
#       "基站的个数是：", myMap.baseStationNum, "\n", "直接统计法错误率是：", de.Mean_value_of_difference(real_density, estimate_density))
# print("程序运行时间为：", end_time - start_time)

EMde = EM_densityEstimation(myMap)
real_density = EMde.realDensity()
estimate_density = EMde.iteration()
print("用户点的个数是：", myMap.userNum, "\n", "基站的个数是：", myMap.baseStationNum, "\n", "EM错误率是：",
      EMde.Mean_value_of_difference(real_density, estimate_density))
end_time = datetime.datetime.now()
print("程序运行时间为：", end_time - start_time)
# a = [0, 1, 2, 3, 4, 5]
# b = []
# b = a
# print(b)

# a = [0, 0, 0, 1]
# computePRR(a)
# print(a)
# computeIRR(a)
# print(a)
# print(np.random.uniform(1, 10, 5000))
# from numpy.random import default_rng
# rng = default_rng()
# print(rng.uniform(1, 1024, 6))
