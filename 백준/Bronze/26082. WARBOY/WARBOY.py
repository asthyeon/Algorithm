import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B, C = map(int, input().split())

print(int(B / A * 3 * C))