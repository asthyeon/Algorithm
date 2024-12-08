import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    universities = {}
    for _ in range(N):
        S, L = map(str, input().split())
        universities[int(L)] = S

    print(universities[max(universities)])