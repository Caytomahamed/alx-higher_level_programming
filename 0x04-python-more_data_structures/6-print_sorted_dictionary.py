#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort = list(a_dictionary)
    sort.sort()

    for x in sort:
          print(f"{x}: {a_dictionary[x]}")
