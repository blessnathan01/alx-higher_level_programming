#!/usr/bin/python3
def weight_average(my_list[]):
    if my_list:
        wt = 0
        deno = 0
        avg = 0
        for i in range(len(my_list)):
            for j in range(len(my_list[i])):
                wt += my_list[i][0] * my_list[i][1]
                deno += my_list[i][1]
        avg = wt / deno
        return avg
    return 0
