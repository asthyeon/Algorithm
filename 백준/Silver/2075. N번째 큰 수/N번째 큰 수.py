import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N번째 큰 수 (2075)
 1. NxN 표에 채워진 수들은 자신의 한 칸 위에 있는 수보다 큼
[입력]
 1. N: 표의 크기
 2. N개의 줄: N개의 수가 주어짐
[출력]
 1. N번째 큰 수 출력
"""

"""
<풀이>
 1. 우선순위큐
 2. 전체를 돌리면 메모리 초과
 3. 힙큐의 길이를 N개로 유지 -> N번째로 큰 숫자를 가장 작은 값으로
"""
import heapq

N = int(input())

# 우선순위큐
hq = []
for _ in range(N):
    table = list(map(int, input().split()))
    
    for number in table:
        # 힙큐의 길이가 N보다 작을 때는 인큐
        if len(hq) < N:
            heapq.heappush(hq, number)
        # 힙큐의 길이가 N일 때
        else:
            # 가장 작은 값이 이번 숫자보다 작거나 같다면 교체
            if hq[0] <= number:
                heapq.heappop(hq)
                heapq.heappush(hq, number)

print(hq[0])
