import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
for tc in range(1, n + 1):
    p = int(input())

    vp = -1
    vn = ''
    for _ in range(p):
        C, name = map(str, input().split())

        if vp < int(C):
            vp = int(C)
            vn = name

    print(vn)
