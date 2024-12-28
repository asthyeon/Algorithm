import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    total = 0

    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())

        total += q * p

    total += s
    print(total)