#!/usr/bin/python3
"""
Module file
"""


def makeChange(coins, total):
    """ function make change"""
    if (total <= 0):
        return 0

    coins.sort(reverse=True)
    tot = 0
    for coin in coins:
        if total == 0:
            break
        mod = total // coin
        total = total - mod * coin
        tot += mod
    return tot if total == 0 else -1
