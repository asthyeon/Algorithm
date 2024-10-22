import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
bread = [input().rstrip() for _ in range(N)]

for n in range(N):
    line = ''
    for m in range(M - 1, -1, -1):
        line += bread[n][m]

    print(line)