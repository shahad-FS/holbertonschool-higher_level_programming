#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return -1
    elif idx > len(my_list):
        return -1
    else:
        value = my_list[idx]
    return value
