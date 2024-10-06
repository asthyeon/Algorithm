import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for x in range(1, T + 1):
    A, B = map(int, input().split())

    print(f'Case {x}: {A + B}')