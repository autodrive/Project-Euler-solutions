# 
# Solution to Project Euler problem 20
# by Project Nayuki
# 
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

import eulerlib


def compute():
    n = eulerlib.factorial(100)
    ans = sum(map(int, str(n)))
    return str(ans)


if __name__ == "__main__":
    print(compute())
