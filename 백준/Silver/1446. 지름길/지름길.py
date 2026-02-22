import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 지름길 (!446)
1. 고속도로에는 지름길이 존재(일방통행)
2. 고속도로는 역주행 불가
3. 세준이가 운전해야 하는 거리의 최솟값 출력

[풀이]
1. 다익스트라
"""
import heapq


def dijkstra(graph):
    distances = [10e9] * (D + 1)
    hq = []
    heapq.heappush(hq, (0, 0))

    while hq:
        now, now_dist = heapq.heappop(hq)

        # 다음 위치 탐색
        for new, new_dist in graph[now]:
            dist = now_dist + new_dist
            # 더 짧은 거리로 도착할 때만 갱신
            if dist < distances[new]:
                distances[new] = dist
                heapq.heappush(hq, (new, dist))

    return distances[D]


N, D = map(int, input().split())
# 각 거리 초기화(다음 위치, 길이)
graph = [[(i + 1, 1)] for i in range(D + 1)]
# 마지막 값 초기화
graph[-1] = []

# 지름길 추가
for _ in range(N):
    start, end, length = map(int, input().split())
    # 고속도로 내에 존재할 때만 추가
    if end <= D:
        graph[start].append((end, length))

print(dijkstra(graph))