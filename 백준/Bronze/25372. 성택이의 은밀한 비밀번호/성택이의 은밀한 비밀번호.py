import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    password = input().rstrip()

    if 6 <= len(password) <= 9:
        print('yes')
    else:
        print('no')