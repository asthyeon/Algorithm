import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] N번째 큰 수
1. 표의 모든 수는 자신의 한 칸 위에 있는 수보다 큼
2. N번째 큰 수를 찾기

[풀이]
1. 우선순위 큐
2. 모든 수를 하나의 리스트로 넣기 -> 메모리 초과
3. 메모리를 N개 길이로 유지
"""
import heapq

N = int(input())
hq = []
for _ in range(N):
    row = list(map(int, input().split()))
    for r in range(N):
        now = row[r]
        # hq 길이가 N개보다 짧다면 인큐
        if len(hq) < N:
            heapq.heappush(hq, now)
        # hq 길이가 N개보다 같거나 크다면 제일 작은걸 빼기
        else:
            new = heapq.heappop(hq)
            heapq.heappush(hq, max(now, new))

# 정답 출력
answer = heapq.heappop(hq)
print(answer)