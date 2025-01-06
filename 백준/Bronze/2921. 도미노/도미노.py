import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

dots = 0
# 위쪽 타일부터 점 세기
for up in range(N + 1):
    for down in range(up, N + 1):
        dots += up + down

print(dots)