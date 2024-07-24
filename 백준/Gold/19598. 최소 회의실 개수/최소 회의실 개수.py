import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최소 회의실 개수 (19598)
 1. N개의 회의를 모두 진행할 수 있는 최소 회의실 개수 구하기
[입력]
 1. N: 배열의 크기
 2. N개의 줄: 시작 시간, 끝나는 시간이 주어짐
[출력]
 1. 최소 회의실 개수 출력
"""

"""
<풀이>
 1. 우선순위큐
"""
import heapq

N = int(input())
rooms = []
for _ in range(N):
    start, end = map(int, input().split())
    rooms.append((start, end))
# 시간순 정렬
rooms.sort()

# 우선순위큐
pq = []
for start, end in rooms:
    # 우선순위큐가 존재하고, 가장 빨리 끝나는 시간이 시작 시간보다 작다면
    if len(pq) > 0 and pq[0] <= start:
        # 이전 회의실 제거
        heapq.heappop(pq)
    # 회의실 추가
    heapq.heappush(pq, end)

print(len(pq))