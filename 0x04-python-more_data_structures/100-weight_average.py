#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum1 = 0
        sum2 = 0
        for i in range(len(my_list)):
            sum1 += my_list[i][0] * my_list[i][1]
            sum2 += my_list[i][1]
        return sum1 / sum2
    return 0
