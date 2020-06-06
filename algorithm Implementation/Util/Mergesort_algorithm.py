

class mergesort_algorithm():



    def Merge_Sort(self,stations):

        length = len(stations)
        middle = int(length/2)

        if length<=1:
            return stations
        else:
            list1 = self.Merge_Sort(stations[:middle])
            list2 = self.Merge_Sort(stations[middle:])

            return self.Merge(list1,list2)




    def Merge(self,list1,list2):
        list3 = []
        length1 = len(list1)
        length2 = len(list2)
        point1 = 0
        point2 = 0


        while point1<=length1-1 and point2<=length2-1:

            if list1[point1].f<list2[point2].f:
                list3.append(list1[point1])
                point1 += 1

            else:
                list3.append(list2[point2])
                point2 += 1

        if point1>=length1:
            for i in range(length2):
                if i>=point2:
                    list3.append(list2[point2])

        if point2>=length2:
            for i in range(length1):
                if i>=point1:
                    list3.append(list1[point1])


        return list3

#def print_sort_result(self):








