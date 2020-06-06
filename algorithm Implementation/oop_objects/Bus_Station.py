
class bus_station():
    '''the class represents the bus station'''



    def __init__(self):
        '''the attribute of name means the name of bus-station
           the attribute of passenger means the passenger now in the bus-station'''

        self.name = "null"
        self.passenger = []
        self.adjacent_station = {}

        #A* algorithm
        self.g = 0
        self.h = 0
        self.f = 0

    def Name(self,name):
        '''change the name of the station'''
        self.name = name

    def add_passengers(self,*passenger):
        '''add the passenger in the bus-station'''
        self.passenger.append(passenger)

    def add_adjacent_station(self,station,edge):
        '''add the adjacent station in the this station'''
        self.adjacent_station[station] = edge

    def get_g(self,value):
        '''get the value of g （线路值）'''
        self.g =value

    def add_g(self,value):
        '''add the valie of g '''
        self.g = self.g+value

    def get_h(self,value):
        '''get the value of f （预估值）'''
        self.h = value

    def result_f(self):
        '''print the value of f （实际值）'''
        self.f = self.g+self.h

    def clean_data(self):
        '''clear the g,h,f to zero'''
        self.h = 0
        self.g = 0
        self.result_f()

    def add_self_cost(self):
        self.add_adjacent_station()




