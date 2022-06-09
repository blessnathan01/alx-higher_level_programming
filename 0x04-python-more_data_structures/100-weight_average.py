#!/usr/bin/python3
def weight_average(my_list[]):
        if my_list:
        weight = 0
        denomt = 0
        avg = 0

        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                weight += my_list[i][0] * my_list[i][1]
                denomt += my_list[i][1]
        avg = weight / denomt
        return avg
    return 0
