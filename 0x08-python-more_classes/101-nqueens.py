#!/usr/bin/python3
import sys

"""Solve the N queens problem by placing N non-attacking queens on an NxN
chessboard.
"""


if len(sys.argv) != 2:
    sys.stderr.write("Usage: nqueens N\n")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    sys.stderr.write("N must be a number\n")
    sys.exit(1)

if N < 4:
    sys.stderr.write("N must be at least 4\n")
    sys.exit(1)


output = []


def solveNQueens(a_list, excluded):
    r = len(a_list)
    if r < N:
        for c in range(N):
            if (r, c) in excluded:
                continue

            ex = set()
            tmp = ('.'*c) + "Q" + ("." * (N - c - 1))

            for r1 in range(r, N):
                ex.add((r1, c))

            r2 = r3 = r
            c2 = c3 = c

            while c2 < N:
                r2 += 1
                c2 += 1
                ex.add((r2, c2))

            while c3 > 0:
                r3 += 1
                c3 -= 1
                ex.add((r3, c3))

            solveNQueens(a_list + [tmp], excluded | ex)
    else:
        output.append(a_list)


def convertOutput():
    result = []
    i = 0
    while i < len(output):
        r = 0
        sub_list = []
        for string in output[i]:
            c = 0
            for char in string:
                if char == 'Q':
                    sub_list.append([r, c])
                    break
                c += 1
            r += 1
        result.append(sub_list)
        i += 1

    return result


def showOutput():
    for row in output:
        print(row)


solveNQueens([], set())
output = convertOutput()
showOutput()
