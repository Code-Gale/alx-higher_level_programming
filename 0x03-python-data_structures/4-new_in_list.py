#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    update = my_list[:]
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    update[idx] = element
    return update
