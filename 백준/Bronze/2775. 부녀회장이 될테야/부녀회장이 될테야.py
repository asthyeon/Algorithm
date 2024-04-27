import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

apart = [[0] * 14 for _ in range(15)]
for floor in range(15):
    if floor == 0:
        number = 0
        for room in range(14):
            number += 1
            apart[floor][room] = number
    else:
        for room in range(14):
            apart[floor][room] = sum(apart[floor - 1][:room + 1])

T = int(input())
for tc in range(1, T + 1):
    k = int(input())
    n = int(input())

    print(apart[k][n - 1])
