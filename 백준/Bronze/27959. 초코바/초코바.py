import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
if 100 * N >= M:
    print('Yes')
else:
    print('No')