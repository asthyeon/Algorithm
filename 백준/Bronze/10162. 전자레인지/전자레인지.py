import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())

A = T // 300
if T % 300 == 0:
    print(A, 0, 0)
    exit()

B = (T % 300) // 60
if (T % 300) % 60 == 0:
    print(A, B, 0)
    exit()

C = ((T % 300) % 60) // 10
if ((T % 300) % 60) % 10 == 0:
    print(A, B, C)
    exit()

print(-1)
