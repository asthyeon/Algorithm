import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최대 힙 (11279)
1. 최대힙
"""
import  heapq

# 연산 수와 힙
N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    
    # 0 연산
    if x == 0:
        # 힙이 있을 때와 비어 있을 때
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    # 그 외 연산은 자연수 추가
    else:
        heapq.heappush(heap, (-x, x))
