



class road():

    def __init__(self,start_station,end_station,settings):
        '''初始化距离和信息素'''
        self.start_station = start_station
        self.end_station = end_station
        self.distance = 0
        self.pheromone = 0
        self.settings = settings
        self.ant_brain_change_value = 0


    def create_road(self):
        '''对应坐标信息素的生成'''
        #Generation of corresponding coordinate pheromones
        distance_matrix = self.settings.station_matrix

        #更新矩阵里面的数值

        #对应的距离
        length = len(distance_matrix[self.start_station])

        for item1 in range(length):
            for item2 in range(length):
                if int(item1) == int(self.start_station):
                    if int(item2) == int(self.end_station):
                        self.distance = 1/distance_matrix[int(item1)][int(item2)]
                        self.pheromone = self.settings.pheromone_matrix[int(item1)][int(item2)]
        #对应的信息素生成，默认添加食物后，不同的点信息素含量会改变
        self.ant_brain_change_value = (self.distance**self.settings.alpha)*(self.pheromone**self.settings.beta)
        return self.ant_brain_change_value


