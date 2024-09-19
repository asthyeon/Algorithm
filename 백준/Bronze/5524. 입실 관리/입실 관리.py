import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    S = input().rstrip()

    print(S.lower())