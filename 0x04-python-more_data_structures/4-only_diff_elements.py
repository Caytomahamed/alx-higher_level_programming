#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    common = set_1.union(set_2)
    for x in set_1:
        for y in set_2:
            if x == y:
                common.remove(x)
    return common