import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

nh, nm, ns = map(int, input().split(':'))
sh, sm, ss = map(int, input().split(':'))

# 초
s = ss - ns
if s < 0:
    s = 60 + s
    nm += 1

# 분
m = sm - nm
if m < 0:
    m = 60 + m
    nh += 1

# 시간
h = sh - nh
if h < 0:
    h = 24 + h

print(f'{h:02}:{m:02}:{s:02}')