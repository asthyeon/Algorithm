import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 최소 힙 (1927)
1. 연산 규칙
 - 배열에 자연수 x를 넣음
 - x가 0일 때, 배열에서 가장 작은 값 출력 후, 그 값을 배열에서 제거

[풀이]
1. 우선순위 큐 이용
"""
import heapq

N = int(input())
hq = []
for _ in range(N):
    x = int(input())

    # x가 0일 때
    if x == 0:
        # 큐에 수가 있다면 출력
        if hq:
            print(heapq.heappop(hq))
        # 큐에 수가 없다면 0 출력
        else:
            print(0)
    # x가 자연수 일때 인큐
    else:
        heapq.heappush(hq, x)

