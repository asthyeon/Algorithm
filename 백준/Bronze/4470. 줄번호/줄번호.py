import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    line = input().rstrip()

    print(f'{i}. {line}')