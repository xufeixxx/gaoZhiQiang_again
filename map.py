import sys

from setting import *
import random
# from numpy.random import default_rng  # 官方文档默认写法
from object.U_Point import UserPoint
from object.BS_Point import BaseStationPoint
from object.distance import DistanceBetweenTwoPoint
from util.lengthTwoPoints import computeTwoPointDis
from util.minDistance import computeMinDistance_BS_ID
from util.randomResponse import computeIRR, computePRR
from util.uniformDistribution import *


class MyMap:
    def __init__(self):
        setts = Settings()
        # self.rng = default_rng()
        self.xRange = setts.map_Xrange
        self.yRange = setts.map_Yrange
        self.U_list = []
        self.BS_list = []
        self.userNum = setts.UserPointNum
        self.baseStationNum = setts.BaseStationPointNum

    def generateUsersPoint(self):
        """
        for i in range(self.userNum):
            ranX = random.randint(1, self.xRange)
            ranY = random.randint(1, self.yRange)
            userPoint = UserPoint(i + 1, ranX, ranY, self.baseStationNum)
            userPoint.init_A()
            self.U_list.append(userPoint)
        """
        if self.userNum == 4000:
            kk = UserPoint_is_4000()
            for i in range(self.userNum):
                ranX = kk[i].x
                ranY = kk[i].y
                userPoint = UserPoint(i + 1, ranX, ranY, self.baseStationNum)
                userPoint.init_A()
                self.U_list.append(userPoint)
        elif self.userNum == 40000:
            kk = UserPoint_is_40000()
            for i in range(self.userNum):
                ranX = kk[i].x
                ranY = kk[i].y
                userPoint = UserPoint(i + 1, ranX, ranY, self.baseStationNum)
                userPoint.init_A()
                self.U_list.append(userPoint)
        elif self.userNum == 400000:
            kk = UserPoint_is_400000()
            for i in range(self.userNum):
                ranX = kk[i].x
                ranY = kk[i].y
                userPoint = UserPoint(i + 1, ranX, ranY, self.baseStationNum)
                userPoint.init_A()
                self.U_list.append(userPoint)
        else:
            print("用户数量异常，只能是4000，40000，400000")
            sys.exit()

    def generateBaseStationPoint(self):
        """
        for i in range(self.baseStationNum):
            ranX = random.randint(1, self.xRange)
            ranY = random.randint(1, self.yRange)
            baseStationPoint = BaseStationPoint(i + 1, ranX, ranY)
            self.BS_list.append(baseStationPoint)
        """
        if self.baseStationNum == 4:
            kk = BaseStation_is_4()
            for i in range(self.baseStationNum):
                ranX = kk[i].x
                ranY = kk[i].y
                baseStationPoint = BaseStationPoint(i + 1, ranX, ranY)
                self.BS_list.append(baseStationPoint)
        elif self.baseStationNum == 40:
            kk = BaseStation_is_40()
            for i in range(self.baseStationNum):
                ranX = kk[i].x
                ranY = kk[i].y
                baseStationPoint = BaseStationPoint(i + 1, ranX, ranY)
                self.BS_list.append(baseStationPoint)
        elif self.baseStationNum == 400:
            kk = BaseStation_is_400()
            for i in range(self.baseStationNum):
                ranX = kk[i].x
                ranY = kk[i].y
                baseStationPoint = BaseStationPoint(i + 1, ranX, ranY)
                self.BS_list.append(baseStationPoint)
        else:
            print("ERROR:基站数量异常，只能是4，40，400")
            sys.exit()

    def userPoint_set_A(self):
        for US in self.U_list:
            dis_list = []
            for BS in self.BS_list:
                dis = computeTwoPointDis(US, BS)
                dis_two_point = DistanceBetweenTwoPoint(dis, US.UP_id, BS.BS_id)
                dis_list.append(dis_two_point)
            bsID = computeMinDistance_BS_ID(dis_list)
            US.BS_id = bsID
            US.A[bsID - 1] = 1
            for i in range(len(US.A)):
                US.R.append(US.A[i])

    def userPoint_set_R(self):
        for userP in self.U_list:
            computePRR(userP.R)
            for i in range(len(userP.R)):
                userP.U.append(userP.R[i])

    def userPoint_set_U(self):
        for userP in self.U_list:
            computeIRR(userP.U)
