# 
# Solution to Project Euler problem 47
# by Project Nayuki
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import itertools

import eulerlib


def compute():
    for i in itertools.count():
        if all((count_distinct_prime_factors(i + j) == 4) for j in range(4)):
            return str(i)


distinctprimefactorscache = {}


def count_distinct_prime_factors(n):
    if n not in distinctprimefactorscache:
        count = 0
        x = n
        while x > 1:
            count += 1
            for i in range(2, eulerlib.sqrt(x) + 1):
                if x % i == 0:
                    x //= i
                    while x % i == 0:
                        x //= i
                    break
            else:
                break  # x is prime
        distinctprimefactorscache[n] = count
    return distinctprimefactorscache[n]


if __name__ == "__main__":
    print(compute())
