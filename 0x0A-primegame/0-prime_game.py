#!/usr/bin/python3

"""prime GAme python"""


def is_prime(n):
    """checks if a num given n is a prime number"""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def calc_prime(n, primes):
    """ claculate primes """
    top = primes[-1]
    if (n > top):
        for i in range(top + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(n, numbers):
    """return the name of the winner"""
    players = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    calc_prime(max(numbers), primes)

    for round in range(n):
        somme = sum((i != 0 and i <= numbers[round])
                    for i in primes[:numbers[round] + 1])

        if (somme % 2):
            win = "Maria"
        else:
            win = "Ben"

        if win:
            players[win] += 1
    if players["Maria"] > players["Ben"]:
        return "Maria"
    elif players["Ben"] > players["Maria"]:
        return "Ben"

    return None
