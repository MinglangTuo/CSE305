
from oop_objects.Ant_Objects.Road import road

import random


class ant():

    def __init__(self,bus_stations,settings,ants_name):
        self.passed_city = []
        #环游次数
        #Travel times
        self.name = ants_name
        #蚂蚁的名字
        #Ant's name
        self.current_city= 0
        #正处于城市中
        # in the city
        self.inital_city = 0
        #初始城市的位置
        # Location of the original city
        #初始点到其他点位置的可能性
        self.other_cities = []

        self.settings = settings

        #随机生成的数值，代表蚂蚁接下来要去哪个点
        self.random_rate = 0.0


        self.denominator = 0
        #其他各个点的值的总和
        #The sum of the values of the other points

        #蚂蚁爬过的路线
        self.route=[]
        #The route that ants travel
        #蚂蚁爬过的路径总长度
        self.length = 0

        #这个路径里面的有关车站
        self.bus_stations = bus_stations

        #蚂蚁分子的值
        self.molecular = {}
        #The value of the ant molecule

        #走过所有路径所需要的时间
        self.time = 0
        #The time it takes to travel all the paths
    def initial_city_method(self):
        '''初始化蚂蚁城市'''
        #Initialize ant city
        random.seed(self.settings.seed)
        station_name = random.randint(1,self.settings.bus_station_number)-1
        self.settings.seed = self.settings.seed + 1

        self.inital_city = station_name
        self.route.append(self.inital_city)
        self.current_city = self.inital_city

    def change_current_city(self,station_name):
        '''改变现有城市到现在的城市'''
        #Change the existing city to the present city
        self.current_city = station_name

    def back_to_initial_city(self):
        self.route.append(self.inital_city)
        self.change_current_city(self.inital_city)


    def select_city(self):
        '''随机选择下一个城市'''

        #初始化改点到各个点的距离
        #distance_matrix = self.settings.station_matrix
            #计算式子里面分母的值（各个路线的　信息素＋道路长度）
        self.calculate_denominator()
            #随机生成一个（０－１）概率的值
        random.seed(self.settings.seed)
        self.random_rate = random.randint(1,10)-1
        self.random_rate = self.random_rate/10
        self.settings.seed = self.settings.seed+1




            # 遍历整个周围节点，
        for item in self.other_cities:
            for key,value in self.molecular.items():
                if key == item:
                    try:
                        rate = value/self.denominator
                        # ｉｆ　如果该概率的值小于该节点的概率，则输出该节点，表示下一步走这个点
                        if rate >= self.random_rate:

                            self.route.append(item)
                            self.change_current_city(item)
                            return item
                        # ｅｌｓｅ改点概率的随机值减去这个节点的概率值，继续运行遍历
                        else:

                            self.random_rate = self.random_rate - rate

                    except ZeroDivisionError:
                        print("the denominator is zero!")





    def calculate_denominator(self):
        '''计算分母的值'''
        #Calculate the value of the denominator
        for item in self.bus_stations:
            if int(item.name) == self.current_city:
                for key,value in item.adjacent_station.items():
                    if int(key.name) not in self.route:
                        self.other_cities.append(int(key.name))

        # 计算分母的值
        for item in self.other_cities:

            rate = road(self.current_city, item,self.settings)
            rate_value = rate.create_road()
            self.molecular[item] = rate_value
            self.denominator = self.denominator + rate_value


    def calculate_route(self):
        '''计算蚂蚁爬过总长度'''
        #Calculate the total length of the ant
        length = len(self.route)
        for item in range(length-1):
            #for item1 in range(self.settings.bus_station_number):
                #for item2 in range(self.settings.bus_station_number):
                    #if item1 == int(self.route[item+1]) and item2 == int(self.route[item]):
            self.length = self.length+self.settings.station_matrix[self.route[item]][self.route[item+1]]
    
    
    def calculate_criteria(self):
        '''计算每个蚂蚁爬行所选长度后，运送乘客所需要的时间'''
        #Calculate the time it takes to transport passengers after each ant crawls its chosen length
        self.criteria_lines()



        # 计算整个线路所花费的评判标准，以乘客所需要的时间为主要目标




    def criteria_lines(self):
        '''the total time for all the passengers to arrive their destination'''

        for start_location in range(self.settings.bus_station_number):
            for dest_location in range(self.settings.bus_station_number):
                criteria = self.settings.passenger_matrix[start_location][dest_location]
                if int(criteria) == 0:
                    pass
                else:
                    for i in range(int(criteria)):
                        passenger_length = self.criteria_calculation(start_location,dest_location)
                        self.time += passenger_length/self.settings.bus_speed
                        #print(self.time)


    def criteria_calculation(self,start_location,dest_location):
        '''calculate the criteria'''
        index1 = 0
        index2 = 0
        lines = self.route.copy()
        lines.pop()
        length = len(lines)

        for item in range(length):
            if lines[item] == start_location:
                index1 = item
            if lines[item] == dest_location:
                index2 = item

        if index1<=index2:
            return self.calculate_route_length(lines,index1,index2)
        else:
            return self.calculate_route_length(lines,index2,index1)


    def calculate_route_length(self,lines,index1,index2):
        '''calculate the criteria'''
        total_length = 0
        total_length_1 = 0
        total_length_2 = 0


        bias = index2 -index1+1
        lines1 =lines[index1:index2+1]
        length_1 = len(lines1)
        length_2 = len(lines)-bias
        for item in range(length_1-1):
            total_length_1 += self.settings.station_matrix[lines[index1]][lines[index1+1]]
            index1 = index1 + 1

        for item in range(length_2+1):
            total_length_2 += self.settings.station_matrix[lines[index1 % len(lines)]][lines[(index1-1) % len(lines)]]
            index1 = index1 - 1


        if total_length_1>total_length_2:
            total_length = total_length_2
        else:
            total_length = total_length_1

        return total_length


    def print_info_ant(self):
        '''print the information about the route for each ant now'''
        total_item = "the name of ant: "+str(self.name)+" :"

        for item in self.route:
            total_item =total_item+"-->"+str(item)
        print(total_item)

    def clear_data(self):
        '''clear the relevant data'''

        self.other_cities = []
        self.denominator =0
        self.molecular = {}
        self.random_rate = 0.0


    def judge_initial_final_station(self):
        '''whether the initial station is same as the final station'''
        if int(self.inital_city) == int(self.current_city):
            return True
        else:
            return False

    def clear_iteration_data(self):
        '''declare thr route in iteration'''
        self.route = []
        self.length = 0
        self.time = 0
        self.route.append(self.current_city)