import csv
import numpy as np
import math

class csv_util():
    #self.station_matrix = None
    #self.passenger_matrix = None
    #self.bus_busy_matrix = None
    #self.pheromone_matrix = None


    def write_station_csv(self,string,setting):
        '''write the station matrix to csv.file'''
        list = []
        k = 0

        f = open(string+".csv",'w',encoding='utf-8',newline='' "")

        csv_writer = csv.writer(f)
        length = setting.bus_station_number
        for i in range(length):
            for j in range(length):
                list.append(setting.station_matrix[i][j])
            csv_writer.writerow(list)
            list = []
        f.close()


    def write_passenger_csv(self,string,setting):
        '''write the passenger matrix to csv.file'''
        list = []
        k = 0

        f = open(string+".csv",'w',encoding='utf-8',newline='' "")

        csv_writer = csv.writer(f)
        length = setting.bus_station_number
        for i in range(length):
            for j in range(length):
                list.append(setting.passenger_matrix[i][j])
            csv_writer.writerow(list)
            list = []
        f.close()


    def write_bus_busy_csv(self,string,setting):
        '''write the bus_busy to csv.file'''
        list = []
        k = 0

        f = open(string+".csv",'w',encoding='utf-8',newline='' "")

        csv_writer = csv.writer(f)
        length = setting.bus_station_number
        for i in range(length):
            for j in range(length):
                list.append(setting.bus_busy_matrix[i][j])
            csv_writer.writerow(list)
            list = []
        f.close()

    def write_pheromone_csv(self, string, setting):
        '''write the pheromone_matrix to csv.file'''
        list = []
        k = 0

        f = open(string + ".csv", 'w', encoding='utf-8', newline='' "")

        csv_writer = csv.writer(f)
        length = setting.bus_station_number
        for i in range(length):
            for j in range(length):
                list.append(setting.pheromone_matrix[i][j])
            csv_writer.writerow(list)
            list = []
        f.close()

    def write_points_csv(self, string, setting,matrix):
        '''write the pheromone_matrix to csv.file'''
        list = []
        k = 0
        f = open(string + ".csv", 'w', encoding='utf-8', newline='' "")

        csv_writer = csv.writer(f)
        length = setting.bus_station_number
        new_matrix_cp = self.handle_matrix(matrix,length)
        for i in range(length):
            for j in range(length):
                list.append(new_matrix_cp[i][j])
            csv_writer.writerow(list)
            list = []
        f.close()

    def write_line_csv(self,lines,string):
        '''write the lines to csv.file'''
        list = []
        k = 0
        f = open(string + ".csv", 'w', encoding='utf-8', newline='' "")

        csv_writer = csv.writer(f)

        for i in lines:
            for j in i:
                list.append(j)
            csv_writer.writerow(list)
            list = []
        f.close()

    def write_sub_lines_csv(self, lines, string):
        '''write the sub_lines to csv.file'''
        list = []
        k = 0
        f = open(string + ".csv", 'w', encoding='utf-8', newline='' "")

        csv_writer = csv.writer(f)

        for i in lines:
            for j in i:
                list.append(j)
            csv_writer.writerow(list)
            list = []
        f.close()




    def generate_coordinate_point(self,matrix):
        '''transfer the distance matrix to the real coordinate points'''
        gram_matrix = self.calculate_gram_matrix(matrix)
        a, b = np.linalg.eig(gram_matrix)
        #b = b.astype(np.int16)
        #a = a.astype(np.int16)
        eigen_vector = format(b)

        length = a.size
        tmp_matrix = np.zeros(length * length)
        random_point_matrix = tmp_matrix.reshape(length, length)

        for item1 in range(length):
            if int(a[item1]) == -0:
                a[item1] = 0
            random_point_matrix[item1][item1] = a[item1]

        #print("the eigen-value is: " + format(random_point_matrix))
        #print("-------------")
        #print("the eigen-vector is: " + eigen_vector)
        #print("-------------")
        sqat_eight_value = np.sqrt(random_point_matrix)
        sqat_eight_value = np.nan_to_num(sqat_eight_value)
        new_matrix = np.dot(b,sqat_eight_value)

        #print("the coordinate points: "+format(new_matrix))
        return new_matrix


    def calculate_gram_matrix(self,matrix):
        '''get the gram matrix for transfer to the coordinate points'''

        length = matrix[0].size
        tmp_matrix = np.zeros(length*length)
        gram_matrix = tmp_matrix.reshape(length,length)

        for item1 in range(length):
            for item2 in range(length):
                gram_matrix[item1][item2] = (math.pow(matrix[0][item2],2)+math.pow(matrix[0][item1],2)-math.pow(matrix[item1][item2],2))/2
                if gram_matrix[item1][item2]<0.1 and gram_matrix[item1][item2]>-0.1:
                    gram_matrix[item1][item2] = 0

        return gram_matrix


    def handle_matrix(self,matrix,length):
        '''handle the data of matrix'''

        matrix_cp = np.zeros(length * length)
        random_point_matrix_cp = matrix_cp.reshape(length, length)


        new_matrix_1 = self.transfer_data_in_matrix(matrix)
        for i in range(length):
            k = 0
            if i == 0:
                continue
            for j in range(length):

                if str(new_matrix_1[i][j]) == "0j":
                    continue
                str_1 = str(new_matrix_1[i][j])
                new_str = str_1[1:]
                new_str_list = new_str.split("+")
                new_matrix_1[i][j] = 0
                random_point_matrix_cp[i][k] = float(new_str_list[0])
                k = k+1
        return random_point_matrix_cp


    def transfer_data_in_matrix(self,matrix):
        '''cut the string in the matrix'''
        str1 = str(matrix[0][0])
        str2 = str1[0:1]
        matrix[0][0] = int(str2)

        str3 =str(matrix[0][1])
        str4 = str3[0:1]
        matrix[0][1] = float(str4)
        return matrix