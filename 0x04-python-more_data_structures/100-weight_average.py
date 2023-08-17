#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        num = 0
        dem = 0
        for turple in my_list:
            num += (turple[0] * turple[1])
            dem += turple[1]
        return (num / dem)
    return 0
