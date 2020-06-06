from Util.Mergesort_algorithm import mergesort_algorithm
import numpy as np
class route_algorithm():
    '''generate the route to optimise the profiles'''

    def __init__(self,settings):
        self.settings = settings

        # a* algorithm sequence
        self.open_list = []
        self.route = []

        #a* brain_judge

        self.flag_find = False
        self.tmp_nodes = []

        #print_parameter
        #self.lines = []

        # merge_sort algorithm
        self.mergesort_algorithm = mergesort_algorithm()


    def A_STAR_Algorithm(self, start_location, dest_location,bus_stations):
        '''search the best route for each passenger to the destination'''

        self.route = []
        self.flag_find = False
        self.clean_f(bus_stations)
        # initial the value of f in start_location
        for item in bus_stations:
            if int(item.name) == start_location:
                item.get_g(0)
                for key, value in item.adjacent_station.items():
                    if int(key.name) == dest_location:
                        item.get_h(value)


        self.open_list.append(start_location)
        #start_location is the name of station



        while self.flag_find == False:
            successor = self.open_list[0]
            self.open_list.remove(successor)
            self.route.append(successor)
            self.voluation_station(successor, dest_location,bus_stations)
            self.tmp_nodes = self.a_brain_judge_1(dest_location,bus_stations)
            #需要打印出来排序的数字
            print(self.flag_find)

            if self.flag_find == True:
                #end the location
                self.route.append(dest_location)
                #add the line to the self.line
                self.print_lines()

                self.open_list = []
                return self.route

            else:
                #continue to search the minimize
                list = self.sort(self.tmp_nodes)
                print("MergeSort:")
                for item in list:
                    print(item.name)
                    #print(item.f)
                #疑问如果前两个的预估值一样该如何处理
                self.open_list.append(int(list[0].name))







    def voluation_station(self, successor, dest_location,bus_stations):
        '''initilize all the f(g+h) to the specific nodes'''

        if len(self.route)>1:
            self.assign_value_successor(bus_stations)
        else:
            pass

        length = len(self.settings.station_matrix[successor])
        for end_element in range(length):
            if end_element == successor:
                pass
            else:
                for station in bus_stations:
                    if int(station.name) == end_element:
                        station.add_g(self.settings.station_matrix[successor][end_element])
                        length_station = len(self.settings.station_matrix[end_element])
                        for element_station in range(length_station):
                            if element_station == dest_location:
                                station.get_h(self.settings.station_matrix[end_element][dest_location])

        for element in bus_stations:
            element.result_f()
        return bus_stations


    def a_brain_judge_1(self, dest_location,bus_stations):
        '''whether the direct_line is the optimize'''
        tmp_dest = bus_stations[0]
        self.tmp_nodes = []
        self.flag_find = True

        for element in bus_stations:
            if int(element.name) == dest_location:
                tmp_dest = element

        for element in bus_stations:
            if element == tmp_dest:
                pass
            else:
                if element.f < tmp_dest.f:
                    self.tmp_nodes.append(element)
                    self.flag_find = False

        if self.flag_find == True:
            #self.route.append(tmp_dest.name)
            return None
        else:
            return self.tmp_nodes


    def sort(self,bus_stations):
        '''sort all the f in the next stations'''
        return self.mergesort_algorithm.Merge_Sort(bus_stations)



    def print_lines(self):
        #print(len(self.route))
        for item in self.route:
            print(item)
        print("NEXT PASSENGER!---------")


    def clean_f(self,stations):
        #clean the all the value about g, h and f.
        for item in stations:
            item.clean_data()

    def assign_value_successor(self,stations):
        #transfer the value of h(initial station to successor station)
        length = self.length_stations(self.route)
        arr = np.array(self.route)

        for item1 in stations:
            if int(item1.name) in self.route:
                item1.get_g(99999)
            else:
                item1.get_g(length)


    def length_stations(self,self_route):
        #calculate the total_length in route
        length = len(self_route)
        total_length = 0
        index = 0
        for i in range(length-1):
            total_length += self.settings.station_matrix[int(self_route[index])][int(self_route[index+1])]

        return total_length




