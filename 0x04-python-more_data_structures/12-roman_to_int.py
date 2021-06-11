#!/usr/bin/python3
def roman_to_int(roman_string):

    romanValues = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    retNum = 0

    if roman_string is not None and isinstance(roman_string, str):
        for index in range(len(roman_string)):
            if index > 0 and romanValues[roman_string[index]] >\
                    romanValues[roman_string[index - 1]]:
                retNum += romanValues[roman_string[index]] - 2 *\
                        romanValues[roman_string[index - 1]]
            else:
                retNum += romanValues[roman_string[index]]
    return retNum
