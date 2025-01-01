import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
star = 0
space = N

for i in range(2 * N - 1):
    if i < N:
        star += 1
        space -= 1
    else:
        star -= 1
        space += 1

    print('*' * star + ' ' * space * 2 + '*' * star)
