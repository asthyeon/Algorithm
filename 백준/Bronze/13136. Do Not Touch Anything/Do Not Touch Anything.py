import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

R, C, N = map(int, input().split())

row = R // N
col = C // N
if R % N > 0:
    row += 1
if C % N > 0:
    col += 1
    
print(row * col)