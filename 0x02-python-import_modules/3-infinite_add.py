#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    n_Args = len(argv)
    sum = 0

    if n_Args > 1:
        for i in range(1, n_Args):
            sum += int(argv[i])

    print(sum)
