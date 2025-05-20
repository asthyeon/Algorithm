import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최소 힙 (1927)
1. 최소힙
"""
import heapq

hq = []
# 연산 정보
N = int(input())
for _ in range(N):
    x = int(input())

    # 0 연산
    if x == 0:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    # 그 외 연산
    else:
        heapq.heappush(hq, x)