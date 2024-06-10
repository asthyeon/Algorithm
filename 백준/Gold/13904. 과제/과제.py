import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 과제 (13904)
 1. 하루에 한 과제를 끝낼 수 있는데, 마감일이 지난 과제는 못 끝냄
 2. 과제마다 끝냈을 때 얻을 수 있는 점수가 있음
[입력]
 1. N: 과제 수
 2. N개의 줄: d: 과제 마감일까지 남은 일수, w: 과제의 점수
[출력]
 1. 얻을 수 있는 점수의 최댓값
"""

"""
<풀이>
 1. 일단 풀어보기 -> 우선순위 큐 사용하기
 2. 날짜를 언제까지 라고 기한이 안남아있음 -> 모든 과제를 건드려볼 수 있음
"""

import heapq
from collections import deque

N = int(input())
assignments = []
for _ in range(N):
    d, w = map(int, input().split())

    assignments.append((d, w))
# 정렬 후 q로 만들기
assignments = deque(sorted(assignments))

# 지난 날과 우선순위 큐
day = 0
hq = []
# 과제가 남아있을 때
while assignments:
    day += 1

    # 과제가 남아있다면
    while assignments:
        # 마감일과 같은 날 일 때
        if assignments[0][0] == day:
            # 우선순위 큐에 과제 넣기
            heapq.heappush(hq, assignments.popleft()[1])
        # 같은 날이 없다면 종료
        else:
            break

    # 우선순위 큐의 길이가 더 크다면
    while len(hq) > day:
        # 작은 순으로 제거
        heapq.heappop(hq)

print(sum(hq))
