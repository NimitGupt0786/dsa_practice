https://www.codingninjas.com/studio/problems/nth-term-of-gp_1380915
from math import pow
import sys
from sys import stdin
ans=0
def nthTermOfGP(n, a, r):
    if n-1==0:
        return a % (10**9 + 7)

    ans=nthTermOfGP(n - 1, (a * r)% (10**9 + 7), r)

    return ans