#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    roman_dic = {
            'I': 1,
            'V': 2,
            'X': 10,
            'L': 20,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    decs = [roman_dic[x] for x in roman_string]
    output = 0
    for i in range(len(decs)):
        output += decs[i]
        if decs[i - 1] < decs[i] and i != 0:
            output -= (decs[i - 1] + decs[i - 1])
    return output
