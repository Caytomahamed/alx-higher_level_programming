#!/usr/bin/python3  
def roman_to_int(roman_string):
    integer = 0;

    if  isinstance(roman_string,str):
        for char in roman_string:
            if char == 'I':
                integer += 1
            elif char == 'V':
                integer += 5
            elif char == 'X':
                integer += 10
            elif char == 'L':
                integer += 50
            elif char == 'C':
                integer += 100
            elif char == 'D':
                integer += 500
            elif char == 'M':
                integer += 100
    else:
        return None
    return integer