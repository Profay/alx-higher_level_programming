#!/usr/bin/python3
def roman_to_int(roman_string):
    dico = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    pre = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    for i in range(len(roman_string) - 1, -1, -1):
        if roman_string[i] not in dico or roman_string[i] is None:
            return 0
        if dico[roman_string[i]] >= pre:
            sum += dico[roman_string[i]]
            pre = dico[roman_string[i]]
        else:
            sum -= dico[roman_string[i]]
    return sum
