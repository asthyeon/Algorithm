import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

order = 1
cnt = 1
while True:
    if N <= order:
        print(cnt)
        break

    order += cnt * 6
    cnt += 1