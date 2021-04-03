class UserPoint:

    def __init__(self, UP_id, x, y, bs_num):
        self.UP_id = UP_id
        self.x = x
        self.y = y
        self.A = []
        self.R = []
        self.U = []
        self.BS_id = 0  # 距离最近的基站的ID
        self.BS_num = bs_num

    # 初始化列表，全部为零
    def init_A(self):
        for i in range(self.BS_num):
            self.A.append(0)

    # def init_R(self):
    #     for i in range(self.BS_num):
    #         self.R.append(0)
    #
    # def init_U(self):
    #     for i in range(self.BS_num):
    #         self.U.append(0)
