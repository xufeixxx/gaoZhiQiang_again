import numpy as np


def computeTwoPointDis(userPoint, baseStationPoint):
    return np.sqrt(np.square(userPoint.x - baseStationPoint.x) + np.square(userPoint.y - baseStationPoint.y))
