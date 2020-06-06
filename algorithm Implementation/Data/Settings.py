
class settings():
    def __init__(self):

        #基本的输入参数
        #Basic input parameters
        self.seed = 5
        self.bus_station_number = 20
        self.passengers_number = 30
        self.edge_distance = 50

        #生成对应的矩阵表示
        #Generate the corresponding matrix
        self.station_matrix = None
        self.passenger_matrix = None
        self.bus_busy_matrix = None
        self.pheromone_matrix = None




        #蚁群算法的相关参数
        #Relevant parameters of ant colony algorithm
        self.pheromone = 10.0
        self.alpha = 2
        self.beta = 3
        self.Volatile_coefficient = 0.3
        #每只蚂蚁所携带信息素总量
        #The amount of pheromones carried by each ant
        self.ant_pheromone_quality = 300.0
        # Q:每只蚂蚁所携带的信息素总量
        self.Q = 300.0
        # 生成蚂蚁的数目
        #The number of ants
        self.ants_number = 20
        # 迭代次数
        self.max_iteration = 10

        #公交汽车的速度
        #the speed of bus
        self.bus_speed = 10
        #行人行走的速度
        #the speed of walking
        self.passengers_speed = 2
        #cut shortest line
        self.cutting_edge = 5

    def value_change(self,pheromone,alpha,beta,volatile_coefficient,ant_pheromone_quality,ant_number):
        '''change the parameters about the ant-colony-algorithm'''

        self.pheromone = pheromone
        self.alpha = alpha
        self.beta = beta
        self.Volatile_coefficient = volatile_coefficient
        # 每只蚂蚁所携带信息素总量
        self.ant_pheromone_quality = ant_pheromone_quality
        # Q:每只蚂蚁所携带的信息素总量
        self.Q = ant_pheromone_quality
        # 生成蚂蚁的数目
        self.ants_number = ant_number








