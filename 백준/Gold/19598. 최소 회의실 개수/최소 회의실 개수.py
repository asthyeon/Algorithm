import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 최소 회의실 개수 (19598)
1. 한 회의가 끝나는 것과 동시에 다음 회의 시작 가능
2. N개의 회의를 모두 진행할 수 있는 최소 회의실 개수 구하기

[풀이]
1. 우선순위 큐
2. 시작 시간순 리스트 순회, 끝나는 순으로 hq에 넣기
3. hq에서 제일 빨리 끝나는 것과 비교하여 못넣게 되면 회의실 추가 
"""
import heapq

N = int(input())
# 현재 리스트(시작 시간순), 우선순위 큐
meetings = [tuple(map(int, input().split())) for _ in range(N)]
meetings.sort()
hq = []

cnt = 0
while meetings:
    start, end = heapq.heappop(meetings)

    # hq가 비어있다면
    if not hq:
        # 회의실 추가 및 인큐, 다음으로 넘기기
        cnt += 1
        heapq.heappush(hq, (end, start))
        continue

    # 가장 빨리 끝나는 회의 꺼내기
    m_end, m_start = heapq.heappop(hq)

    # 이번 미팅을 시작할 수 있다면 바로 인큐
    if start >= m_end:
        heapq.heappush(hq, (end, start))
    # 이번 미팅을 시작할 수 없다면 회의실 추가, 이전 미팅도 재추가
    else:
        cnt += 1
        heapq.heappush(hq, (end, start))
        heapq.heappush(hq, (m_end, m_start))

print(cnt)