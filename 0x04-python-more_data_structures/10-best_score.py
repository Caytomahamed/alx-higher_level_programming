#!/usr/bin/python3
def best_score(a_dictionary):
    largestInt = 0;
    key = 0;
    if a_dictionary == None:
        return None
    else:
        for idx, value in a_dictionary.items():
            if largestInt < value:
                largestInt = value
                key = idx
    return key
