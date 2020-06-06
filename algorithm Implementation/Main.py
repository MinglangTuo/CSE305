from oop_objects.Route import route
from Util.Ant_Algorithm import ant_algorithm
from Util.Csv_Util import csv_util
import csv
import multiprocessing

def display_one_demo_line():

    new_route = route()
    new_route.start_route()
    new_csv_util = csv_util()

    print("The distance between different bus station :")
    new_route.bus_stations_matrix()

    print("The location information for passengers :")
    new_route.passengers_matrix()
    settings = new_route.busy_route_matrix()
    passenger_route = new_route.passengers_route

    #跑完完整一条路线所显示的
    new_ant_algorithm = ant_algorithm(settings)
    new_ant_algorithm.travel_the_cities(new_route.bus_stations)
    # 当划分线段为６的时候程序出错
    new_ant_algorithm.cutting_edge(4, passenger_route)
    new_ant_algorithm.print_final_cut_lines()









    # 多进程用在这部分

    # 生成相关csv文件
    #new_csv_util.write_station_csv("station_matrix", settings)
    #new_csv_util.write_passenger_csv("passenger_matrix", settings)
    new_csv_util.write_bus_busy_csv("bus_busy_matrix", settings)
    #new_csv_util.write_pheromone_csv("pheromone_matrix", settings)

    # 生成笛卡尔坐标


    new_matrix = new_csv_util.generate_coordinate_point(settings.station_matrix)
    new_csv_util.write_points_csv("points_matrix", settings, new_matrix)

    lines = new_ant_algorithm.return_csv_lines()
    new_csv_util.write_line_csv(lines, "lines")

    sub_lines = new_ant_algorithm.return_sub_csv_lines()
    new_csv_util.write_sub_lines_csv(sub_lines, "sub_lines")






def calculate_twenty_stations_part4():
    ''':parameter'''
    pheromone = 10.0


    new_route = route()
    new_route.start_route()
    new_csv_util = csv_util()

    print("The distance between different bus station :")
    new_route.bus_stations_matrix()

    print("The location information for passengers :")
    new_route.passengers_matrix()
    settings = new_route.busy_route_matrix()
    passenger_route = new_route.passengers_route

    # 把数据写入csv文件中
    f = open("dataSet_part1.csv", "w", encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ["Bus_Numbers", "Passenger_Number", "Iteration_Times", "Pheromone", "Alpha", "Beta", "Volatile_Coefficient",
         "Ant_Pheromone_Quality", "Ants_Number", "Shortest_Line", "shortest_Time", "Cut_Lines", "Cut_Times"])

    # 手动设置setting各项的数值，来让蚁群算法跑
    for pheromone_number in range(3):
        pheromone = pheromone + 5
        alpha = 2
        for alpha_number in range(5):
            alpha = alpha + 1
            beta = 2

            for beta_number in range(5):
                beta = beta + 1
                Volatile_coefficient = 0.3
                for cofficient_number in range(5):
                    Volatile_coefficient = Volatile_coefficient + 0.1
                    Q = 100.0
                    ant_pheromone_quality = 100.0
                    for Q_number in range(5):
                        Q = Q + 90
                        ant_pheromone_quality = ant_pheromone_quality + 15
                        ants_number = 20
                        for ant in range(3):
                            ants_number = ants_number + 5
                            settings.value_change(pheromone, alpha, beta, Volatile_coefficient,
                                                  ant_pheromone_quality, ants_number)

                            new_ant_algorithm = ant_algorithm(settings)
                            new_ant_algorithm.travel_the_cities(new_route.bus_stations)
                            # 当划分线段为６的时候程序出错
                            new_ant_algorithm.cutting_edge(4, passenger_route)
                            new_ant_algorithm.print_final_cut_lines()

                            csv_writer.writerow([str(settings.bus_station_number), str(settings.passengers_number),
                                                 str(settings.max_iteration), str(pheromone), str(alpha), str(beta),
                                                 str(Volatile_coefficient), str(ant_pheromone_quality), str(ants_number)
                                                    , str(new_ant_algorithm.shortest_lines),
                                                 str(new_ant_algorithm.time), str(new_ant_algorithm.shortest_cut_lines),
                                                 str(new_ant_algorithm.cut_time)])

    f.close()

    '''

        # 多进程用在这部分

        # 生成相关csv文件
        new_csv_util.write_station_csv("station_matrix", settings)
        new_csv_util.write_passenger_csv("passenger_matrix", settings)
        new_csv_util.write_bus_busy_csv("bus_busy_matrix", settings)
        new_csv_util.write_pheromone_csv("pheromone_matrix", settings)

        # 生成笛卡尔坐标
        #

        new_matrix = new_csv_util.generate_coordinate_point(settings.station_matrix)
        new_csv_util.write_points_csv("points_matrix", settings, new_matrix)

        lines = new_ant_algorithm.return_csv_lines()
        new_csv_util.write_line_csv(lines, "lines")

        sub_lines = new_ant_algorithm.return_sub_csv_lines()
        new_csv_util.write_sub_lines_csv(sub_lines, "sub_lines")

        # rw = renderwindow()

        # rw.main()
        '''


def calculate_twenty_stations_part5():
    ''':parameter'''
    pheromone = 40


    new_route = route()
    new_route.start_route()
    new_csv_util = csv_util()

    print("The distance between different bus station :")
    new_route.bus_stations_matrix()

    print("The location information for passengers :")
    new_route.passengers_matrix()
    settings = new_route.busy_route_matrix()
    passenger_route = new_route.passengers_route

    # 把数据写入csv文件中
    f = open("dataSet_part2.csv", "w", encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ["Bus_Numbers", "Passenger_Number", "Iteration_Times", "Pheromone", "Alpha", "Beta", "Volatile_Coefficient",
         "Ant_Pheromone_Quality", "Ants_Number", "Shortest_Line", "shortest_Time", "Cut_Lines", "Cut_Times"])

    # 手动设置setting各项的数值，来让蚁群算法跑
    for pheromone_number in range(3):
        pheromone = pheromone + 5
        alpha = 2
        for alpha_number in range(5):
            alpha = alpha + 1
            beta = 2

            for beta_number in range(5):
                beta = beta + 1
                Volatile_coefficient = 0.3
                for cofficient_number in range(5):
                    Volatile_coefficient = Volatile_coefficient + 0.1
                    Q = 100.0
                    ant_pheromone_quality = 100.0
                    for Q_number in range(5):
                        Q = Q + 90
                        ant_pheromone_quality = ant_pheromone_quality + 15
                        ants_number = 20
                        for ant in range(3):
                            ants_number = ants_number + 5
                            settings.value_change(pheromone, alpha, beta, Volatile_coefficient,
                                                  ant_pheromone_quality, ants_number)

                            new_ant_algorithm = ant_algorithm(settings)
                            new_ant_algorithm.travel_the_cities(new_route.bus_stations)
                            # 当划分线段为６的时候程序出错
                            new_ant_algorithm.cutting_edge(4, passenger_route)
                            new_ant_algorithm.print_final_cut_lines()

                            csv_writer.writerow([str(settings.bus_station_number), str(settings.passengers_number),
                                                 str(settings.max_iteration), str(pheromone), str(alpha), str(beta),
                                                 str(Volatile_coefficient), str(ant_pheromone_quality), str(ants_number)
                                                    , str(new_ant_algorithm.shortest_lines),
                                                 str(new_ant_algorithm.time), str(new_ant_algorithm.shortest_cut_lines),
                                                 str(new_ant_algorithm.cut_time)])

    f.close()

    '''

        # 多进程用在这部分

        # 生成相关csv文件
        new_csv_util.write_station_csv("station_matrix", settings)
        new_csv_util.write_passenger_csv("passenger_matrix", settings)
        new_csv_util.write_bus_busy_csv("bus_busy_matrix", settings)
        new_csv_util.write_pheromone_csv("pheromone_matrix", settings)

        # 生成笛卡尔坐标
        #

        new_matrix = new_csv_util.generate_coordinate_point(settings.station_matrix)
        new_csv_util.write_points_csv("points_matrix", settings, new_matrix)

        lines = new_ant_algorithm.return_csv_lines()
        new_csv_util.write_line_csv(lines, "lines")

        sub_lines = new_ant_algorithm.return_sub_csv_lines()
        new_csv_util.write_sub_lines_csv(sub_lines, "sub_lines")

        # rw = renderwindow()

        # rw.main()
        '''


def calculate_twenty_stations_part6():
    ''':parameter'''
    pheromone = 55


    new_route = route()
    new_route.start_route()
    new_csv_util = csv_util()

    print("The distance between different bus station :")
    new_route.bus_stations_matrix()

    print("The location information for passengers :")
    new_route.passengers_matrix()
    settings = new_route.busy_route_matrix()
    passenger_route = new_route.passengers_route

    # 把数据写入csv文件中
    f = open("dataSet_part3.csv", "w", encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ["Bus_Numbers", "Passenger_Number", "Iteration_Times", "Pheromone", "Alpha", "Beta", "Volatile_Coefficient",
         "Ant_Pheromone_Quality", "Ants_Number", "Shortest_Line", "shortest_Time", "Cut_Lines", "Cut_Times"])

    # 手动设置setting各项的数值，来让蚁群算法跑
    for pheromone_number in range(3):
        pheromone = pheromone + 5
        alpha = 2
        for alpha_number in range(5):
            alpha = alpha + 1
            beta = 2

            for beta_number in range(5):
                beta = beta + 1
                Volatile_coefficient = 0.3
                for cofficient_number in range(5):
                    Volatile_coefficient = Volatile_coefficient + 0.1
                    Q = 100.0
                    ant_pheromone_quality = 100.0
                    for Q_number in range(5):
                        Q = Q + 90
                        ant_pheromone_quality = ant_pheromone_quality + 15
                        ants_number = 20
                        for ant in range(3):
                            ants_number = ants_number + 5
                            settings.value_change(pheromone, alpha, beta, Volatile_coefficient,
                                                  ant_pheromone_quality, ants_number)

                            new_ant_algorithm = ant_algorithm(settings)
                            new_ant_algorithm.travel_the_cities(new_route.bus_stations)
                            # 当划分线段为６的时候程序出错
                            new_ant_algorithm.cutting_edge(4, passenger_route)
                            new_ant_algorithm.print_final_cut_lines()

                            csv_writer.writerow([str(settings.bus_station_number), str(settings.passengers_number),
                                                 str(settings.max_iteration), str(pheromone), str(alpha), str(beta),
                                                 str(Volatile_coefficient), str(ant_pheromone_quality), str(ants_number)
                                                    , str(new_ant_algorithm.shortest_lines),
                                                 str(new_ant_algorithm.time), str(new_ant_algorithm.shortest_cut_lines),
                                                 str(new_ant_algorithm.cut_time)])

    f.close()

    '''

        # 多进程用在这部分

        # 生成相关csv文件
        new_csv_util.write_station_csv("station_matrix", settings)
        new_csv_util.write_passenger_csv("passenger_matrix", settings)
        new_csv_util.write_bus_busy_csv("bus_busy_matrix", settings)
        new_csv_util.write_pheromone_csv("pheromone_matrix", settings)

        # 生成笛卡尔坐标
        #

        new_matrix = new_csv_util.generate_coordinate_point(settings.station_matrix)
        new_csv_util.write_points_csv("points_matrix", settings, new_matrix)

        lines = new_ant_algorithm.return_csv_lines()
        new_csv_util.write_line_csv(lines, "lines")

        sub_lines = new_ant_algorithm.return_sub_csv_lines()
        new_csv_util.write_sub_lines_csv(sub_lines, "sub_lines")

        # rw = renderwindow()

        # rw.main()
        '''


def calculate_twenty_stations_part1():
    ''':parameter'''
    pheromone = 70


    new_route = route()
    new_route.start_route()
    new_csv_util = csv_util()

    print("The distance between different bus station :")
    new_route.bus_stations_matrix()

    print("The location information for passengers :")
    new_route.passengers_matrix()
    settings = new_route.busy_route_matrix()
    passenger_route = new_route.passengers_route

    # 把数据写入csv文件中
    f = open("dataSet_part4.csv", "w", encoding='utf-8', newline='' "")
    csv_writer = csv.writer(f)
    csv_writer.writerow(
        ["Bus_Numbers", "Passenger_Number", "Iteration_Times", "Pheromone", "Alpha", "Beta", "Volatile_Coefficient",
         "Ant_Pheromone_Quality", "Ants_Number", "Shortest_Line", "shortest_Time", "Cut_Lines", "Cut_Times"])

    # 手动设置setting各项的数值，来让蚁群算法跑
    for pheromone_number in range(3):
        pheromone = pheromone + 5
        alpha = 2
        for alpha_number in range(5):
            alpha = alpha + 1
            beta = 2

            for beta_number in range(5):
                beta = beta + 1
                Volatile_coefficient = 0.3
                for cofficient_number in range(5):
                    Volatile_coefficient = Volatile_coefficient + 0.1
                    Q = 100.0
                    ant_pheromone_quality = 100.0
                    for Q_number in range(5):
                        Q = Q + 90
                        ant_pheromone_quality = ant_pheromone_quality + 15
                        ants_number = 20
                        for ant in range(3):
                            ants_number = ants_number + 5
                            settings.value_change(pheromone, alpha, beta, Volatile_coefficient,
                                                  ant_pheromone_quality, ants_number)

                            new_ant_algorithm = ant_algorithm(settings)
                            new_ant_algorithm.travel_the_cities(new_route.bus_stations)
                            # 当划分线段为６的时候程序出错
                            new_ant_algorithm.cutting_edge(4, passenger_route)
                            new_ant_algorithm.print_final_cut_lines()

                            csv_writer.writerow([str(settings.bus_station_number), str(settings.passengers_number),
                                                 str(settings.max_iteration), str(pheromone), str(alpha), str(beta),
                                                 str(Volatile_coefficient), str(ant_pheromone_quality), str(ants_number)
                                                    , str(new_ant_algorithm.shortest_lines),
                                                 str(new_ant_algorithm.time), str(new_ant_algorithm.shortest_cut_lines),
                                                 str(new_ant_algorithm.cut_time)])

    f.close()

    '''

        # 多进程用在这部分

        # 生成相关csv文件
        new_csv_util.write_station_csv("station_matrix", settings)
        new_csv_util.write_passenger_csv("passenger_matrix", settings)
        new_csv_util.write_bus_busy_csv("bus_busy_matrix", settings)
        new_csv_util.write_pheromone_csv("pheromone_matrix", settings)

        # 生成笛卡尔坐标
        #

        new_matrix = new_csv_util.generate_coordinate_point(settings.station_matrix)
        new_csv_util.write_points_csv("points_matrix", settings, new_matrix)

        lines = new_ant_algorithm.return_csv_lines()
        new_csv_util.write_line_csv(lines, "lines")

        sub_lines = new_ant_algorithm.return_sub_csv_lines()
        new_csv_util.write_sub_lines_csv(sub_lines, "sub_lines")

        # rw = renderwindow()

        # rw.main()
        '''


if __name__ == "__main__":
    display_one_demo_line()






    '''
    pool = multiprocessing.Pool(processes=4)

    pool.apply_async(calculate_twenty_stations_part6)

    pool.apply_async(calculate_twenty_stations_part5)

    pool.apply_async(calculate_twenty_stations_part4)

    pool.apply_async(calculate_twenty_stations_part1)

    pool.apply_async((), (4,))

    pool.close()
    pool.join()
    '''


