import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 싸지방에 간 준하 (12764)
 1. 컴퓨터는 1번 부터 순서대로 번호가 매겨짐
 2. 모든 사람은 싸지방에 들어왔을 때 비어있는 자리 중에서 번호가 가장 작은 자리에 앉는 것이 규칙
[입력]
 1. N: 사람 수
 2. N개의 줄: P: 각 사람의 이용 시작 시각, Q: 각 사람의 종료 시작
[출력]
 1. X: 모든 사람이 기다리지 않아도 되는 컴퓨터의 최소 개수
 2. 1번 자리부터 X번 자리까지 순서대로 각 자리를 사용한 사람의 수를 띄어쓰기 간격으로 출력
"""

"""
<풀이>
 1. 우선순위큐
"""
import heapq

N = int(input())
# 시작시간 순서로 담은 우선순위큐
start = []
for _ in range(N):
    P, Q = map(int, input().split())
    heapq.heappush(start, (P, Q))

# 컴퓨터 최소 개수, 각 컴퓨터 사용자 수, 각 컴퓨터 종료 시간
cnt = 0
user = [0] * (N + 1)
time = [0] * (N + 1)

# 우선순위큐 순회
while start:
    s, e = heapq.heappop(start)
    # 순회
    for i in range(1, N + 1):
        # 시작시간이 더 크다면
        if s >= time[i]:
            # 사용자가 한 명도 없다면
            if not time[i]:
                cnt += 1
            time[i] = e
            user[i] += 1
            break

print(cnt)
print(*user[1:cnt + 1])