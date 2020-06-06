from Util.Random_Algorithm import random_algorithm
from Data.Settings import settings

from Util.Route_Algorithm import route_algorithm
import numpy as np


class route():

    def __init__(self):
        self.bus_stations = []
        self.passengers = []
        self.settings = settings()

        #random algorithm
        self.random_algorithm = random_algorithm()
        self.passengers_route = []



        #route_algorithm
        self.route_algorithm = route_algorithm(self.settings)



    def start_route(self):
        '''The raw route Information(TEXT) for bus_stations '''


        stations = self.random_algorithm.random_station(self.settings.bus_station_number)
        finsih_edge_stations = self.random_algorithm.random_edge(stations)
        '''
        for item in finsih_edge_stations:
            print("\nthe information for " + item.name + " is: \t")
            for key, value in item.adjacent_station.items():
                print("the station is " + key.name)
                print("   the distace is " + str(value))
        '''
        self.bus_stations = finsih_edge_stations

        '''The raw route Information(Text) for passengers'''
        self.passengers = self.random_algorithm.random_passenger(self.settings.passengers_number)


    def bus_stations_matrix(self):
        '''trasfer the raw text to the matrix'''
        #create zero_matrix
        length = len(self.bus_stations)
        tmp_matrix = np.zeros(length*length)
        station_matrix = tmp_matrix.reshape(length,length)

        for item in self.bus_stations:
            for key,value in item.adjacent_station.items():
                station_matrix[int(item.name)][int(key.name)] = value
                station_matrix[int(key.name)][int(item.name)] = value
        print(station_matrix)
        self.settings.station_matrix = station_matrix


    def passengers_matrix(self):
        '''trasfer the raw text to the matrix'''
        length = len(self.bus_stations)
        tmp_matrix = np.zeros(length*length)
        passenger_matrix = tmp_matrix.reshape(length,length)

        for item in self.passengers:
            #print("the start location of passenger is "+str(item.name))
            #print("the end location of passenger is "+str(item.end_location))
            #print("   ")
            passenger_matrix[item.name-1][item.end_location-1]+=1;

        print(passenger_matrix)
        self.settings.passenger_matrix = passenger_matrix


    def busy_route_matrix(self):
        '''generate the bus_busy_route matrix'''

        # create zero_matrix
        length = len(self.bus_stations)
        tmp_matrix = np.zeros(length * length)
        bus_busy_matrix = tmp_matrix.reshape(length, length)
        tmp_route = []

        #read the requirements of passengers
        length = self.settings.bus_station_number
        for start_location in range(length):
            for dest_location in range(length):
                if self.settings.passenger_matrix[start_location][dest_location] == 0:
                    pass
                else:
                    magnitude = self.settings.passenger_matrix[start_location][dest_location]
                    #运行a*算法去寻找最短路径
                    tmp_route = self.route_algorithm.A_STAR_Algorithm(start_location,dest_location,self.bus_stations)
                    #assign the value to the bus_busy_matrix
                    self.assign_value_bus_busy_matrix(bus_busy_matrix,magnitude,tmp_route)
                    self.passengers_route.append(tmp_route)
        self.settings.bus_busy_matrix = bus_busy_matrix
        print("The number of passengers in the bus_busy_matrix")
        print(bus_busy_matrix)
        return self.settings


    def practice(self):
        '''practice some programming'''
        for element in self.bus_stations:
            print((element.f))


    def assign_value_bus_busy_matrix(self,bus_busy_matrix,magnitude,tmp_route):
        length = len(tmp_route)

        for i in range(length-1):
            bus_busy_matrix[tmp_route[i]][tmp_route[i+1]] += magnitude;
            bus_busy_matrix[tmp_route[i+1]][tmp_route[i]] += magnitude;




