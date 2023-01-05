#!/usr/bin/python3
from sys import argv

n_Args = len(argv)
if n_Args > 1:
    if (n_Args == 2):
        print("1 argument:")
    elif (n_Args > 2):
        print("{} arguments:".format(n_Args - 1))
    for i in range(1, n_Args):
        print("{0}: {1}".format(i, argv[i]))
else:
    print("0 arguments.")
