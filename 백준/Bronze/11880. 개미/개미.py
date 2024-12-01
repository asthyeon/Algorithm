import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())

    one = a ** 2 + (b + c) ** 2
    two = b ** 2 + (c + a) ** 2
    thr = c ** 2 + (a + b) ** 2

    print(min(one, two, thr))