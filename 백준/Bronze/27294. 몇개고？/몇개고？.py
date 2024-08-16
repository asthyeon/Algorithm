import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T, S = map(int, input().split())

if 12 <= T <= 16:
    if not S:
        print(320)
    else:
        print(280)
else:
    print(280)