import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 강의실 (1374)
 1. 최대한 적은 수의 강의실을 사용하여 모든 강의가 이루어지게 하기
 2. 한 강의실에서는 동시에 2개 이상의 강의를 진행할 수 없음
 3. 한 강의의 종료시간과 다른 강의의 시작시간이 겹치는 것은 상관 없음
[입력]
 1. N: 강의의 수
 2. N개의 줄: 강의 번호, 시작 시간, 종료 시간
[출력]
 1. 필요한 최소 강의실 개수
"""

"""
<풀이>
 1. 우선순위큐
"""
import heapq

N = int(input())
lessons = []
for _ in range(N):
    number, start, end = map(int, input().split())
    # 시작 시간 순서대로 집어넣기
    lessons.append((start, end))
lessons.sort()

# 끝나는 시간을 기록할 우선순위큐
hq = []
# 강의 순회
for lesson in lessons:
    # 첫 강의 집어넣기
    if not hq:
        heapq.heappush(hq, lesson[1])
    else:
        # 가장 빨리 끝나는 시간보다 이번 강의의 시작 시간이 더 빠르다면
        if hq[0] > lesson[0]:
            # 이번 강의의 끝나는 시간을 새로 넣기 (강의실 늘리기)
            heapq.heappush(hq, lesson[1])
        # 가장 빨리 끝나는 시간보다 이번 강의의 시작 시간이 같거나 느리다면
        else:
            # 강의실 교체
            heapq.heappop(hq)
            heapq.heappush(hq, lesson[1])

# 필요한 강의실 개수 출력
print(len(hq))
