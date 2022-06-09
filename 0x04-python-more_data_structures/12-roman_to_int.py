#!/usr/bin/python3


# roman_to_int - converts a roman numeral to an integer.
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000,\
'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    if roman_string and type(roman_string) == str:
        n = 0
        for i in range(len(roman_string)):
            for j in romans.keys():
                if roman_string[:] is j:
                    n = romans[j]
                    return n
                if roman_string[i:i+1] is j:
                    n += romans[j]
                    break
        return n
    else:
        return 0
