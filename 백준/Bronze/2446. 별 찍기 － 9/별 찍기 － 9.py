import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
star = 2 * N + 1
space = -1

for i in range(2 * N - 1):
    if i < N:
        star -= 2
        space += 1
    else:
        star += 2
        space -= 1

    print(' ' * space + '*' * star)
