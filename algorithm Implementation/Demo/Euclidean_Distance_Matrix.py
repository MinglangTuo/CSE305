import numpy as np
import math
import itertools
import random


class euclidean_distance_matrix():


    def points_matrix_demo2_cp(self,length):
        '''transfer the 10 points to the matrix'''

        random_list = list(itertools.product(range(1, 100), range(1, 100)))
        list_new = random.sample(random_list, length)

        tmp_matrix = np.zeros(length * length)
        distance_matrix = tmp_matrix.reshape(length, length)

        for item1 in range(length):
            for item2 in range(length):
                if item1 == item2:
                    pass
                distance_matrix[item1][item2] = self.calculate_euclidean_distance(list_new[item1], list_new[item2])

        return distance_matrix




    def calculate_euclidean_distance(self,point_A,point_B):
        '''calculate distance between two points'''
        distance = math.sqrt(math.pow(point_A[0]-point_B[0],2)+math.pow(point_A[1]-point_B[1],2))
        return distance






