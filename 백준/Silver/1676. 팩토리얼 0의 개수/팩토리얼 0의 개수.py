import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

N = int(input())
string_N = str(math.factorial(N))

cnt = 0
for i in range(len(string_N) - 1, -1, -1):
    if string_N[i] == '0':
        cnt += 1
    else:
        print(cnt)
        break