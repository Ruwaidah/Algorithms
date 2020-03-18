#!/usr/bin/python

import argparse


def find_max_profit(prices):
    print(prices)
    max_price = prices[1]
    min_price = prices[0]
    index = 1
    for i in range(len(prices)):
        if max_price < prices[i] and i > 0:
            max_price = prices[i]
            index = i
    for a in range(index):
        if prices[a] < min_price:
            min_price = prices[a]
    return max_price - min_price


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
