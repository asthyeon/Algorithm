import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for tc in range(1, N + 1):
    r, e, c = map(int, input().split())
    ad = e - c

    if ad > r:
        print('advertise')
    elif ad < r:
        print('do not advertise')
    else:
        print('does not matter')