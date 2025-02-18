import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+ 1):
    N, string = input().split()

    print(string[:int(N) - 1] + string[int(N):])