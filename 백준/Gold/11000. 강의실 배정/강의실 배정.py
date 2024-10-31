import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 강의실 배정 (11000)
 1. 최소의 강의실을 사용해서 모든 수업을 가능하게 하기
 2. 수업이 끝난 직후에 다음 수업을 시작할 수 있음
[입력]
 1. N: 수업의 개수
 2. N개의 줄: S: 시작 시간, T: 끝나는 시간
[출력]
 1. 강의실의 개수 출력
"""

"""
<풀이>
 1. 우선순위 큐
"""
import heapq

N = int(input())
# 수업들 시간
lessons = []
for _ in range(N):
    S, T = map(int, input().split())

    lessons.append((S, T))

# 시작 순으로 정렬
lessons.sort()

# 강의실 배정하기
classes = []
for lesson in range(N):
    # 수업이 배정되어 있을 때
    if classes:
        # 현재 배정된 수업의 끝나는 시간 뒤라면 현재 배정된 수업 제거
        if classes[0] <= lessons[lesson][0]:
            heapq.heappop(classes)

    # 끝나는 시간 배정
    heapq.heappush(classes, lessons[lesson][1])

print(len(classes))
