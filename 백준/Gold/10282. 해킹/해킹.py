import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 해킹(10282)
 1. 컴퓨터 a가 컴퓨터 b에 의존할 시, b가 감염되면 a도 감염
 2. b가 a를 의존하지 않으면 a가 감염되어도 b는 안전
[입력]
 1. 테스트 케이스 수
 2. n: 컴퓨터 수, d: 의존성 수, c: 해킹당한 컴퓨터 번호
 3. d개의 줄: a, b, s: 컴퓨터 a가 컴퓨터 b를 의존, b 감염시 s초 후 a도 감염(단방향)
[출력]
 1. 총 감염 컴퓨터 수, 마지막 컴퓨터가 감염되기까지 걸리는 시간 출력
"""

"""
<풀이>
 1. 다익스트라
"""
import heapq
INF = 10e9


# 다익스트라
def dijkstra(connections, c):
    # 방문 거리 리스트
    distances = [INF] * (n + 1)
    # 힙큐 및 시작점 인큐, 거리 초기화
    hq = [(0, c)]
    distances[c] = 0
    # 총 감염 수(기본 1개)
    cnt = 1

    while hq:
        time, now = heapq.heappop(hq)

        # 다음 컴퓨터 탐색
        for new in connections[now]:
            new_time = time + new[0]
            # 첫 방문이라면 카운트
            if distances[new[1]] == INF:
                cnt += 1
                heapq.heappush(hq, (new_time, new[1]))
                distances[new[1]] = new_time
            # 이미 방문한 곳이라면 카운트 X
            elif distances[new[1]] > new_time:
                heapq.heappush(hq, (new_time, new[1]))
                distances[new[1]] = new_time

    # 마지막 컴퓨터가 감염되는 시간
    last = 0
    for j in range(1, n + 1):
        if distances[j] != INF:
            last = max(last, distances[j])

    return cnt, last


T = int(input())
for tc in range(1, T + 1):
    # 컴퓨터 수 n, 의존성 수 d, 해킹 번호 c
    n, d, c = map(int, input().split())
    # 컴퓨터 연결 관계
    connections = [[] for _ in range(n + 1)]
    for connection in range(d):
        # a가 b를 의존, b 감염시 s초 후 a 감염
        a, b, s = map(int, input().split())
        connections[b].append((s, a))

    # 시간 순서대로 정렬
    for i in range(1, n + 1):
        connections[i].sort()

    print(*dijkstra(connections, c))
