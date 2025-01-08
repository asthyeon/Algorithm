import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

star = '* '
star_n = 1
space = ' '
space_n = N - 1
for i in range(N):
    print(space * space_n + star * star_n)

    space_n -= 1
    star_n += 1