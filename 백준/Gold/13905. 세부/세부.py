import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 세부 (13905)
 1. 최대한의 금빼빼로만을 들고 혜빈이에게 가기
 2. 각 다리는 무게 제한이 존재
[입력]
 1. N: 집의 수, M: 다리 수
 2. s: 출발 위치, e: 도착 위치
 3. M개의 줄: 다리 정보 h1 집과 h2 집은 무게제한이 k인 다리로 연결되어 있음
[출력]
 1. 들고갈 수 있는 금빼빼로 최대 개수 출력
"""

"""
<풀이>
 1. 우선순위큐
 2. 도착지에 도달하지 못하는 경우도 고려하기
"""
import heapq


# 다리 건너기
def bridge(start, end, houses):
    visited = [0] * (N + 1)
    hq = []
    # 시작점 방문 기록 및 출발
    visited[start] = 1
    for new in houses[start]:
        heapq.heappush(hq, (new[0], new[1]))

    # 이후 탐색
    while hq:
        weight, now = heapq.heappop(hq)
        # print(f'weight: {weight}, now: {now}')

        # 도착지라면 종료
        if now == end:
            return -weight

        # 방문한 곳이라면 넘기기
        if visited[now]:
            continue

        # 방문 기록
        visited[now] = 1

        # 다음 장소 탐색
        for new in houses[now]:
            # 방문하지 않은 지역이라면
            if not visited[new[1]]:
                # print(f'real_new: {new[0]} new_weight: {max(weight, new[0])}, new: {new[1]}')
                # 더 작은 값으로 무게 갱신 (음수이므로 더 큰 값으로 이용)
                heapq.heappush(hq, (max(weight, new[0]), new[1]))
                
    # 혜빈이에게 가지 못하면 0개
    return 0


N, M = map(int, input().split())
s, e = map(int, input().split())
# 집 정보
houses = [[] for _ in range(N + 1)]
# 집 연결
for _ in range(M):
    h1, h2, k = map(int, input().split())

    # 음수 값으로 넣어서 무게 제한 맞추기
    houses[h1].append((-k, h2))
    houses[h2].append((-k, h1))

print(bridge(s, e, houses))