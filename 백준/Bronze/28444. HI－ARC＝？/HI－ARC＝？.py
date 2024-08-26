import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

H, I, A, R, C = map(int, input().split())
first = H * I
second = A * R * C

print(first - second)