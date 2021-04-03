from setting import Settings
import math

setts = Settings()


class Theta_base:
    def __init__(self, theta, id):  # id为基站的id
        self.theta = theta
        self.id = id


class C_Density:
    def __init__(self, id, density_num):
        self.id = id
        self.density_num = density_num


class EM_densityEstimation:
    def __init__(self, myMap):
        self.myMap = myMap
        self.Pr_Uk_1_Ak_1 = ((1 - 0.5 * setts.pro_f) * setts.pro_q) + (0.5 * setts.pro_f * setts.pro_p)
        self.Pr_Uk_0_Ak_1 = ((1 - 0.5 * setts.pro_f) * (1 - setts.pro_q)) + (0.5 * setts.pro_f * (1 - setts.pro_p))
        self.Pr_Uk_1_Ak_0 = 0.5 * setts.pro_f * setts.pro_q + ((1 - 0.5 * setts.pro_f) * setts.pro_p)
        self.Pr_Uk_0_Ak_0 = (0.5 * setts.pro_f * (1 - setts.pro_q)) + ((1 - 0.5 * setts.pro_f) * (1 - setts.pro_p))
        self.n = setts.BaseStationPointNum
        self.N = setts.UserPointNum
        self.theta = 1 / self.n
        self.theta_list = []
        for bs in self.myMap.BS_list:
            self.theta_list.append(Theta_base(self.theta, bs.BS_id))

    def computePr_lr_A_xi(self, r, i):
        n = len(self.myMap.BS_list)
        sum_num = 1
        lr = self.myMap.U_list[r - 1].U
        for k in range(n):
            if k + 1 == i:
                sum_num *= pow(self.Pr_Uk_1_Ak_1, lr[k]) * pow(self.Pr_Uk_0_Ak_1, 1 - lr[k])
            else:
                sum_num *= pow(self.Pr_Uk_1_Ak_0, lr[k]) * pow(self.Pr_Uk_0_Ak_0, 1 - lr[k])

        return sum_num

    def E_step(self, r, i):
        theta_sum = 0
        for y in range(self.n):
            theta_sum += self.computePr_lr_A_xi(r, y+1) * self.theta_list[y].theta

        return self.theta_list[i-1].theta*self.computePr_lr_A_xi(r, i)/theta_sum

    def M_step(self, i):
        sum_num = 0
        for r in range(self.N):
            sum_num += self.E_step(r+1, i)

        return 1/self.N*sum_num

    def iteration(self):
        for n in range(10):   # 迭代50次小数点后九位的精度
            for i in range(self.n):
                self.theta_list[i].theta = self.M_step(i + 1)
            print("迭代", n+1, "次")
            for j in range(len(self.theta_list)):
                print(self.theta_list[j].theta)
        return self.theta_list

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
            s_num += abs(real_density[i].density_num - estimate_density[i].theta)

        return s_num/setts.BaseStationPointNum




