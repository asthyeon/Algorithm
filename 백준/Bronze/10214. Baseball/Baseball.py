import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T + 1):
    Yonsei = Korea = 0
    for i in range(9):
        Y, K = map(int, input().split())

        Yonsei += Y
        Korea += K

    if Yonsei > Korea:
        print('Yonsei')
    elif Yonsei < Korea:
        print('Korea')
    else:
        print('Draw')