#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    multiply = 0
    total_weight = 0
    for item in my_list:
        multiply += (item[0] * item[1])
        total_weight += item[1]
    return multiply / total_weight
