#!/usr/bin/python3
import sys

argv = sys.argv

if __name__ == "__main__":
    def print_arg(argv):
        num_args = len(argv)

         if num_args == 1:
            print("Number of argument:.")
        elif num_args == 2:
            print("Number of argument:")
        else:
        print("Number of arguments:")

    for i in range(1, num_args):
        print("{}: {}".format(i, argv[i]))
