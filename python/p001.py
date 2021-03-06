# 
# Solution to Project Euler problem 1
# Copyright (c) Project Nayuki. All rights reserved.
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 
# Modified by Autodrive
#
# Problems: https://projecteuler.net/archives


# Computers are fast, so we can implement this solution directly without any clever math.
def compute():
    return str(sum(set(range(3, 1000, 3) + range(5, 1000, 5))))


if __name__ == "__main__":
    print(compute())
