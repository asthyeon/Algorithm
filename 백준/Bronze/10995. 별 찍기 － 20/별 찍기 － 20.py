import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

star = '* '
for i in range(N):
    if i % 2 == 0:
        print(star * N)
    else:
        print(' ' + star * N)