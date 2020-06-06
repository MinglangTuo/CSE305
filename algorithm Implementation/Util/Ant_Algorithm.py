import numpy as np

from Util.Random_Algorithm import random_algorithm
class ant_algorithm():

    def __init__(self,settings):

        #最短路径
        #The shortest path
        self.shortest_lines = []
        self.shortest_length = 999999
        self.time = 999999
        #随机算法
        self.random_algorithm_ant = random_algorithm()

        #蚂蚁
        self.ants = []

        #遍历所有城市所需要的最短路径
        #The shortest path required to traverse all cities
        self.min_route = []


        self.settings = settings
        '''Settings'''
        #Q:每只蚂蚁所携带的信息素总量
        self.Q = settings.Q
        #生成蚂蚁的数目
        self.ants_number = settings.ants_number
        #迭代次数
        self.max_iteration = settings.max_iteration

        #子线段
        self.sub_line = []

        #乘客花费时间
        self.total_passengers_time = 0

        #最短的划分方式
        self.shortest_cut_lines = []

        #花费时间最少
        self.cut_time = 999999

        #生成csv线路文件
        self.csv_lines = []
        self.csv_line = []

        #生成分线段的线路文件
        self.csv_sub_lines = []
        self.csv_sub_line = []



    def generate_ants(self,bus_station):
        '''生成若干只蚂蚁随机分配在城市中'''
        #Generate a number of ants randomly assigned to the city


        self.ants = self.random_algorithm_ant.random_ants(self.ants_number,bus_station,self.settings)


    def travel_the_cities(self,bus_station):
        '''Determine if the number of iterations is used up'''
        '''判断迭代次数是否用完'''
        #先布置好信息素
        self.add_foods()

        #生成相关随机的蚂蚁
        self.generate_ants(bus_station)

        #是－－>生成线路，最短线路
        #否－－>执行迭代
        iteration = 1
        while iteration<=self.max_iteration:
            # 遍历所有城市（改进版应该只遍历所有有乘客的城市）
            self.csv_line.append(iteration)
            for look in range(self.settings.bus_station_number-1):
                # 对于里面任意一只蚂蚁
                for ant in self.ants:
                    #进行一次轮渡选择法(select_method)
                    self.select_method(ant)
                    ant.clear_data()
                    ant.print_info_ant()
            #让每只蚂蚁回到最初的节点，并且记录总长度
            for ant in self.ants:
                if ant.judge_initial_final_station() == False:
                    ant.back_to_initial_city()

            #把路径赋值给各个蚂蚁
            for ant in self.ants:
                ant.calculate_route()
                ant.calculate_criteria()


            #比较每条路径的长短，把最短路径返回给属性
            for ant in self.ants:
                if self.time>ant.time:
                    self.time = ant.time
                    self.shortest_lines = ant.route
                    print("the mini shortest length has changed: "+str(self.time))
            print(str(self.time))
            self.csv_line.append(str(self.time))

            #update the tmp_shortest_route
            self.calculate_mini_route()
            self.csv_lines.append(self.csv_line)
            self.csv_line = []

            #更新所有道路信息素(update_information_pheromone)
            self.update_information_pheromone()
            iteration = iteration+1

            #把路径还原
            for ant in self.ants:
                ant.clear_iteration_data()




    def select_method(self,ant):
        '''选择随机到的下一个位置'''
        #Select the next location that you randomly go to
        #初始化这个蚂蚁所在城市到各个点的概率_（蚂蚁方法）
        next_city = ant.select_city()
        ant.change_current_city(next_city)

    def update_information_pheromone(self):
        '''更新道路信息素'''
        #Update the road pheromone
        # 应用信息素更新公式：挥发后的信息素＋道路新增加的信息素
        length = self.settings.bus_station_number
        for i in range(length):
            for j in range(length):
                # 挥发后的信息素 = 原来的信息素×挥发系数
                self.settings.pheromone_matrix[i][j] *= self.settings.Volatile_coefficient

        # 道路新增加的信息素 = 每只蚂蚁的信息素总量/道路总长度　？？
        #遍历所有的路线
        for ant in self.ants:
            dp = 0
            try:
                dp = self.settings.ant_pheromone_quality / ant.length
            except ZeroDivisionError:
                print("the length of ant is zero, Please re-set the parameter")
            length = len(ant.route)
            # 前面蚂蚁寻找最短路径的逻辑错误了！
            for item in range(length - 1):
                for item1 in range(self.settings.bus_station_number):
                    for item2 in range(self.settings.bus_station_number):
                        if item1 == int(ant.route[item + 1]) and item2 == int(ant.route[item]):
                            self.settings.pheromone_matrix[ant.route[item1]][ant.route[item2]] += dp
                            self.settings.pheromone_matrix[ant.route[item2]][ant.route[item1]] += dp
            #print(self.settings.pheromone_matrix)









    def add_foods(self):
        '''人为添加食物，去让蚂蚁在有食物的路径上产生更多的信息素,建立信息素矩阵!!!!'''
        #Add food to make ants produce more pheromones in the path of food, build a pheromone matrix
        length = self.settings.bus_station_number
        tmp_matrix = np.zeros(length * length)
        pheromone_matrix = tmp_matrix.reshape(length, length)

        #人为添加食物到所指定的路线上面去
        food_matrix = self.settings.bus_busy_matrix



        #人为初始化各个节点信息素，之后依照a*算法更改节点信息素！！！！
        for i in range(length):
            for j in range(length):

                pheromone_matrix[i][j] = self.settings.pheromone+food_matrix[i][j]*self.settings.pheromone

        self.settings.pheromone_matrix = pheromone_matrix



    def calculate_mini_route(self):
        '''calculate the tmp_shortest route'''
        lines = "The tmp_shortest route is: "
        for item in self.shortest_lines:
            lines = lines+"-->"+str(item)
            self.csv_line.append(item)
        print(lines)


    def cutting_edge(self,line_number,passenger_route):
        '''cutting the edge to the different route'''


        copy_route = self.shortest_lines.copy()
        copy_route.pop()
        length = len(copy_route)
        float_sub_line_length = length/line_number

        if float_sub_line_length%1>0.5 and float_sub_line_length%1 !=0:
            float_sub_line_length +=1

        sub_line_length = int(float_sub_line_length)

        #if sub_line_length != line_number:
        #    sub_line_length = line_number

        total_length = 0
        m = 0

        for i in range(int(sub_line_length)):
            while total_length<length:
                self.sub_line.append(copy_route[m:m+sub_line_length])
                total_length+=sub_line_length
                m+=sub_line_length
            self.calculate_mini_cost_passenger(passenger_route)
            self.print_time()

            self.print_lines()

            #筛选整个路径
            total_length = 0
            m = 0
            element = copy_route[0]
            copy_route.pop(0)
            copy_route.append(element)



    def print_lines(self):
        '''打印出切割的线段有那些'''
        #The line segments that are printed out are those
        for i in self.sub_line:
            subLine = "The sub line is "
            for j in i:
                subLine +=str(j)+"->"
                self.csv_sub_line.append(str(j))
            print(subLine)
            self.csv_sub_lines.append(self.csv_sub_line)
            self.csv_sub_line = []
        print()



        self.sub_line = []

    def criteria_calculation(self,start_location,dest_location,route):
        '''calculate the criteria'''
        index1 = 0
        index2 = 0
        lines = route.copy()
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

    def judge_whether_lines(self,start_location,dest_location,route):
        '''计算两个点在同一路径'''
        #Compute two points in the same path
        if start_location in route and dest_location in route:
            print("the passenger needn't to change the bus!")
            return self.criteria_calculation(start_location,dest_location,route)
        else:
            print("the passenger need to change the bus!")
            return 0





    def calculate_mini_cost_passenger(self,passenger_route):
        '''根据换乘的要求，由三种方案，计算出哪种方案的乘客达所需要的点，时间为最短的'''
        #According to the requirements of the transfer, three schemes are used to work out which one takes the shortest time to reach the required point
        #方案三：每一步都走到最优点，然后判断该点是否在公交车线路上，比较做公交车去目的地和步行去目的地拿个线路时间最短
            #已经读取了每个乘客的到达目的地的最短路径，然后按照最短路径的行程，参考每条路径，如果有公交，就坐公交，没有公交，就去走路完成
                #先去判断这名乘客需不需要换乘，如果不需要换乘，直接计算到两边所花费的时间，如果需要换乘，根据a×算法，比较不同的情况
        self.total_passengers_time = 0
        for route in passenger_route:
            for bus_line in self.sub_line:
                length = self.judge_whether_lines(route[0],route[-1],bus_line)
                self.total_passengers_time += length/ self.settings.bus_speed
                        #计算两个点坐车最小花费时间


                if route[0]in bus_line and route[-1] not in bus_line:
                    for i in range(len(route)-1):
                        length = self.judge_whether_lines(route[i],route[i+1],bus_line)
                        if length ==0:
                            length = self.settings.station_matrix[route[i]][route[i+1]]
                            self.total_passengers_time+=length/self.settings.passengers_speed
                        self.total_passengers_time += length/ self.settings.bus_speed

                        judge_lenght = self.judge_whether_lines(route[i+1],route[-1],bus_line)
                        if judge_lenght !=0:
                            self.total_passengers_time += judge_lenght / self.settings.bus_speed
                            break


    def print_time(self):
        '''print the time-waste for different passengers'''
        print(self.total_passengers_time)
        self.csv_sub_line.append(self.total_passengers_time)
        if self.cut_time>self.total_passengers_time:
            self.cut_time = self.total_passengers_time
            self.shortest_cut_lines = self.sub_line
        #self.total_passengers_time = 0





    def print_final_cut_lines(self):
        print(self.cut_time)
        print(self.shortest_cut_lines)


    def return_csv_lines(self):
        '''return the data of csv_lines'''
        return self.csv_lines

    def return_sub_csv_lines(self):
        return self.csv_sub_lines














