import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 케빈 베이컨의 6단계 법칙
1. 임의의 두 사람이 최소 몇 단계만에 이어질 수 있는지?
2. 케빈 베이컨의 수: 한 사람이 모든 사람과 친구를 맺을 때 거치는 총 단계 수

[풀이]
1. 최단 경로 -> 모든 사람을 대상으로 최단 경로 구하기
"""
import heapq
INF = 10e9


def dijkstra(start, graph):
    distances = [INF] * (N + 1)
    distances[start] = 0
    hq = [(start, distances[start])]

    while hq:
        now, now_dist = heapq.heappop(hq)

        # 현재 방문한 단계가 더 적거나 같을 때만 다음 친구 방문
        if now_dist <= distances[now]:
            for new in graph[now]:
                new_dist = now_dist + 1
                # 다음 친구에게 더 적은 값으로 방문할 수 있을 때 방문
                if new_dist < distances[new]:
                    distances[new] = new_dist
                    heapq.heappush(hq, (new, new_dist))

    # 이번 사람 번호, 이번 사람의 케빈 베이컨 수 반환
    return start, sum(distances[1:])


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 모든 사람의 케빈 베이컨 수
answer = []
# 모든 사람 순회
for i in range(1, N + 1):
    answer.append(dijkstra(i, graph))

# 케빈 베이컨 수로 정렬
answer.sort(key=lambda x: x[1])
# 가장 첫 번째 사람 출력
print(answer[0][0])

