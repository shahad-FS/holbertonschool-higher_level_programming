#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    else:
        for number in range(len(my_list)):
            if my_list[number] > my_list[number + 1]:
                return my_list[number]
            else:
                return my_list[number + 1]
