import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
if N == M:
    print(1)
else:
    print(0)