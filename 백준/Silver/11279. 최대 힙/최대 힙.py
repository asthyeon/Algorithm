import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 최대 힙 (11279)
1. 연산 규칙
 - x: 배열에 자연수 x 넣기
 - 0: 배열에서 가장 큰 값 출력 및 배열에서 그 값 제거
   (배열이 비어있는 경우 0 출력)

[풀이]
1. 우선순위 큐
"""
import heapq

N = int(input())
hq = []
for _ in range(N):
    x = int(input())

    # x가 0이라면
    if x == 0:
        # hq가 비어있지 않다면 가장 큰 값 출력(부호 변환)
        if hq:
            print(-heapq.heappop(hq))
        # hq가 비어있다면 0 출력
        else:
            print(0)
    # x가 자연수라면 음수로 넣기
    else:
        heapq.heappush(hq, -x)