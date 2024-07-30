import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
print(B - A, B)
