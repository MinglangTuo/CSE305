import random
from Data.Settings import  settings
from oop_objects.Bus_Station import bus_station
from oop_objects.Passenger import passenger
from oop_objects.Ant_Objects.Ant import ant
from Demo.Euclidean_Distance_Matrix import euclidean_distance_matrix

class random_algorithm():
    '''generate the random bus-stations and passengers'''

    def __init__(self):
        self.setting = settings()
        self.ants_name = 1
        self.new_euclidean = euclidean_distance_matrix()

    def random_passenger(self,number):
        '''generate random passengers for bus-station,
        and assumes there are 6 stations now. Furthermore, the data will be crawled by the creeper'''
        passengers = []
        for i in range(number):

            new_passenger = passenger()
            random.seed(self.setting.seed)
            new_passenger.Change_Name(random.randint(1,self.setting.bus_station_number))
            # generate the start-location

            self.setting.seed +=1
            end_location = random.randint(1,self.setting.bus_station_number)
            # generate the end-location

            while new_passenger.name == end_location:
                self.setting.seed += 1
                end_location = random.randint(1,self.setting.bus_station_number)
            #judge whether the start-location same as the end-location

            new_passenger.change_end_location(end_location)
            passengers.append(new_passenger)

        return passengers


    def random_station(self,number):
        '''generate the name of random stations '''

        bus_stations = []
        for i in range(number):
            new_bus_station = bus_station()
            new_bus_station.Name(str(i))
            bus_stations.append(new_bus_station)
        return bus_stations


    def random_edge(self,bus_stations):
        '''generate the edge information for the stations'''

        matrix_distance = self.new_euclidean.points_matrix_demo2_cp(len(bus_stations))
        #print("--------------------")
        #print("The distance matrix: ")
        #print(matrix_distance)
        #print("--------------")
        for location1 in bus_stations:
            #print("The information add in "+location1.name)
            for location2 in bus_stations:
                if location1 != location2:
                    #print("the "+location2.name+" was added in the "+location1.name)
                    if location2 not in location1.adjacent_station and location1 not in location2.adjacent_station:

                        edge = matrix_distance[int(location1.name)][int(location2.name)]
                        location1.add_adjacent_station(location2,edge)
                        location2.add_adjacent_station(location1,edge)
                        #print("the edge is "+str(edge))

        return bus_stations

    def random_ants(self,ants_number,bus_station,settings):
        '''Generate random ants that walk around in the matrix'''
        #reate a certain number of ants, randomly generate coordinates,
        # name them random coordinates, add the ant object to the random coordinates
        tmp_ants = []
        for i in range(ants_number):
            new_ant = ant(bus_station,settings,self.ants_name)
            new_ant.initial_city_method()
            tmp_ants.append(new_ant)
            self.ants_name = self.ants_name+1
        return tmp_ants









