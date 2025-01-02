import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
total = 0
for i in range(N):
    tap = int(input())
    total += tap - 1
    if i == N - 1:
        total += 1

print(total)