from map import MyMap
from setting import Settings

setts = Settings()


class C_Density:
    def __init__(self, id, density_num):
        self.id = id
        self.density_num = density_num


#
# class A_Estimate:
#     def __init__(self, id, num_A):
#         self.id = id
#         self.num_A = num_A
class DirectEstimate:
    def __init__(self, myMap):
        self.myMap = myMap

    def DirectStatistics_densityEstimation(self):
        estimate_list = []
        N = setts.UserPointNum
        s_numA = 0
        N_i = 0
        """
        A_Estimates = []
        N = myMap.userNum
        sum = 0
        N_i = 0
        for c in myMap.BS_list:
            for up in myMap.U_list:
                if up.U[c.BS_id - 1] == 1:
                    N_i += 1
            e_num = (1 / (1 - setts.pro_f)) * (((N_i - setts.pro_p * N) / (setts.pro_q - setts.p)) - ((setts.pro_f * N) / 2))
            A_Estimates.append(A_Estimate(c.BS_id, e_num))
            N_i = 0
            sum += e_num

        for c in myMap.BS_list:
            for i in A_Estimates:
                if i.id == c.BS_id:
                    estimate_list.append(C_Estimate(c.BS_id, i.num_A/sum))
        """
        for c in self.myMap.BS_list:
            for up in self.myMap.U_list:
                if up.U[c.BS_id - 1] == 1:
                    N_i += 1
            e_num = (1 / (1 - setts.pro_f)) * (
                    ((N_i - setts.pro_p * N) / (setts.pro_q - setts.pro_p)) - ((setts.pro_f * N) / 2))
            N_i = 0
            s_numA += e_num

        for c in self.myMap.BS_list:
            for up in self.myMap.U_list:
                if up.U[c.BS_id - 1] == 1:
                    N_i += 1
            e_num = (1 / (1 - setts.pro_f)) * (
                    ((N_i - setts.pro_p * N) / (setts.pro_q - setts.pro_p)) - ((setts.pro_f * N) / 2))
            N_i = 0
            estimate_list.append(C_Density(c.BS_id, e_num / s_numA))

        return estimate_list

    def realDensity(self):
        density_list = []
        i = 0
        kk = self.myMap.BS_list
        for c in kk:
            for up in self.myMap.U_list:
                if up.BS_id == c.BS_id:
                    i += 1
            density_list.append(C_Density(c.BS_id, i / setts.UserPointNum))
            i = 0
        return density_list

    def Mean_value_of_difference(self, real_density, estimate_density):
        s_num = 0
        for i in range(setts.BaseStationPointNum):
            s_num += abs(real_density[i].density_num - estimate_density[i].density_num)

        return s_num/setts.BaseStationPointNum




