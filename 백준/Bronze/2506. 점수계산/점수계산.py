import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
solved = list(map(int, input().split()))

total = 0
point = 0
for i in range(N):
    if solved[i]:
        point += 1
    else:
        point = 0

    total += point

print(total)