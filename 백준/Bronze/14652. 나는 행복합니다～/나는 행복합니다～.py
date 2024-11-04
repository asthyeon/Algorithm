import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, K = map(int,  input().split())

row = K // M
col = K % M

print(row, col)