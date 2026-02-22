import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 타임머신 (11657)
1. 순간이동 및 타임머신으로 시간을 되돌아가는 경우가 존재
2. 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간 출력
3. 무한루프의 경우 -1만 출력, 해당 도시로 가는 경로가 없다면 -1 출력

[풀이]
1. 다익스트라 -> 음수 순환 불가
2. 벨만 포드: 매 단계마다 모든 간선을 전부 확인하며 모든 노드 간의 최단 거리를 구함
"""


def bellman_ford(graph):
    # 거리 및 시작점 초기화
    distances = [10e9] * (N + 1)
    distances[1] = 0

    # 도시 수만큼 반복
    for i in range(N):
        # 버스 수만큼 반복
        for j in range(M):
            # 현재 위치, 다음 위치, 거리
            now = graph[j][0]
            new = graph[j][1]
            dist = graph[j][2]
            # 현재 위치에 도달할 수 있다면
            if distances[now] < 10e9:
                # 다음 위치로 더 짧게 방문할 수 있다면 갱신
                if distances[now] + dist < distances[new]:
                    distances[new] = distances[now] + dist
                    # 마지막 라운드에서도 값이 갱신되는 경우 무한 루프로 판단
                    if i == N - 1:
                        return -1

    # 음수 순환이 존재하지 않는 경우
    return distances



N, M = map(int, input().split())
# 그래프 연결
graph = []
for _ in range(M):
    A, B, C = map(int, input().split())
    graph.append((A, B, C))

answer = bellman_ford(graph)

# 음수 순환인 경우
if answer == -1:
    print(answer)
# 음수 순환이 아니라면
else:
    for i in range(2, N + 1):
        # 도달할 수 없다면 -1
        if answer[i] == 10e9:
            print(-1)
            continue
        # 도달할 수 있다면 값 출력
        print(answer[i])