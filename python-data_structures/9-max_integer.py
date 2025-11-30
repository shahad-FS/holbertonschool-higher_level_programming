#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    max_num = 0
    while i < len(my_list):
        if my_list[i] + 1 > len(my_list):
            break
        elif my_list[i] < my_list[i + 1]:
            max_num =  my_list[i + 1]
        elif my_list[i] > my_list[i + 1]:
            max_num = my_list[i]
        i += 1
    return (max_num)
