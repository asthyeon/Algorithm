import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
mark = '*'
star = 0
for i in range((N * 2) - 1):
    if i <= N - 1:
        star += 1
    else:
        star -= 1
    print(mark * star)