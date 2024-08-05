import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for i in range(N, 0, -1):
    print(i * '*')