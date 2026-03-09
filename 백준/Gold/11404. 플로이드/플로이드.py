import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 플로이드 (11404)
1. 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는 데 필요한 비용의 최솟값?
2. 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있음 
3. i에서 j로 갈 수 없는 경우 0 출력 

[풀이]
1. 플로이드워셜: i에서 j로 가는 최소 비용표를 계속 갱신
"""
INF = int(1e9)


def floyd_warshall(graph, n):
    # 경유지 후보 k 순회
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                # 바로 가는 것과 경유하는 것 중 최솟값으로 갱신
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


n = int(input())
m = int(input())
# 그래프 연결
graph = [[INF] * (n + 1) for _ in range(n + 1)]
# 자기 자신 갱신
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # 같은 노선 중 최솟값으로 갱신
    graph[a][b] = min(graph[a][b], c)

floyd_warshall(graph, n)

# 정답 출력
for i in range(1, n + 1):
    answer = []
    for j in range(1, n + 1):
        # 도달하지 못하면 0
        if graph[i][j] == INF:
            answer.append(0)
            continue
        answer.append(graph[i][j])
    print(*answer)