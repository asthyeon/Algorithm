import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    c, v = map(int, input().split())

    print(f'You get {c // v} piece(s) and your dad gets {c % v} piece(s).')