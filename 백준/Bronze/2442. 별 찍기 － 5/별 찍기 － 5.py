import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
mark = '*'
space = N - 1
star = 0
for _ in range(N):
    print((' ' * space) + (mark * star) + mark + (mark * star))

    space -= 1
    star += 1