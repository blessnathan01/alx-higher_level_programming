#!/usr/bin/python3
def roman_to_int(roman_string):
    roms = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,\
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    if roman_string and type(roman_string) == str:
        n = 0
        for x in range(len(roman_string)):
            for y in roms.keys():
                if roman_string[:] is y:
                    n = roms[y]
                    return n
                if roman_string[x: x + 1] is y:
                    n += roms[y]
                    break
        return n
    else:
        return 0
