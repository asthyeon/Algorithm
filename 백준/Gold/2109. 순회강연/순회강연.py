import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 순회강연 (2109)
 1. 각 대학에서는 d일 안에 와서 강연을 하면 p만큼의 강연료를 지불함
 2. 학자는 하루에 최대 한 곳에서만 강연 가능
[입력]
 1. n: 대학 수
 2. n개의 줄: 각 대학에서 제시한 p값과 d값
[출력]
 1. 최대로 벌 수 있는 돈 출력
"""

"""
<풀이>
 1. 일단 풀어보기 -> 정렬
 2. 우선순위 큐를 이용하여 최소 값을 제거 하는 방식
"""
import heapq

n = int(input())
# 대학들
universities = []
for _ in range(n):
    p, d = map(int, input().split())

    # 날짜를 먼저 넣고 날짜를 기준으로 정렬하기
    universities.append((d, p))
universities.sort()

# 우선순위 큐
hq = []
# 대학 순회
for university in universities:
    # 작은 날짜부터 강연료 추가
    heapq.heappush(hq, university[1])
    
    # 강연료를 받은 날이 이번 날짜보다 크다면 최소값 제거 (초과한 것)
    if len(hq) > university[0]:
        heapq.heappop(hq)

# 강연료 최대 값
print(sum(hq))