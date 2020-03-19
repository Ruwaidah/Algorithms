#!/usr/bin/python

import sys


def rock_paper_scissors(n):
    game = ['rock', 'paper', 'scissors']
    possible = []
    if n == 0:
        return [[]]
    if n == 1:
        return [['rock'], ['paper'], ['scissors']]
    base_array = rock_paper_scissors(n-1)
    a = 0
    b = 0
    i = 0
    while a < 3**n:
        if i >= 3:
            i = 0
            b += 1
        if b >= len(base_array):
            b = 0
        # print("basse", n, [*base_array[b], game[i]])
        possible.append([*base_array[b], game[i]])
        i += 1
        a += 1
    return possible


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
        print(len(rock_paper_scissors(num_plays)))
    else:
        print('Usage: rps.py [num_plays]')
