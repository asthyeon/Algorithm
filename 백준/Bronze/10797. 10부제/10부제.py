import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

day = int(input())
cars = list(map(int, input().split()))

cnt = 0
for car in cars:
    if car == day:
        cnt += 1

print(cnt)