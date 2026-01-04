import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 알고리즘 수업 - 깊이 우선 탐색 1
1. DFS로 풀기

[풀이]
1. DFS
2. turn + 1 -> 같은 깊이에서는 같은 순서로 반복해서 중복됨
3. turn을 전역 변수화
"""
# 런타임 에러 해결을 위해 재귀 깊이 변경
sys.setrecursionlimit(10**9)


# sudo 코드로 구성된 dfs 구현
def dfs(visited, graph, now):
    # 방문 순서를 입력
    global turn
    visited[now] = turn
    turn += 1

    # dfs 탐색
    for new in graph[now]:
        if not visited[new]:
            dfs(visited, graph, new)


N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# 그래프 연결
for _ in range(M):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

# 오름차순 방문을 위한 정렬
for g in graph:
    g.sort()

# 방문 리스트
visited = [0] * (N + 1)

# 방문
turn = 1
dfs(visited, graph, R)
# 정답 출력
for i in range(1, N + 1):
    print(visited[i])