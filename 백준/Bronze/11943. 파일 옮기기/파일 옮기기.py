import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

print(min(A + D, B + C))