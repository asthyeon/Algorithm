import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

import math

A, B = map(int, input().split())

print(math.gcd(A, B))
print(math.lcm(A, B))