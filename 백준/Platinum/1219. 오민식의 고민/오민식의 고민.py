import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 오민식의 고민 (1219)
 1. 민식이의 여행 경로 A -> B
 2. 오민식은 모든 교통수단의 출발 도시와 도착 도시를 알고 있음
 3. 오민식은 각각의 도시를 방문할 때마다 벌 수 있는 돈을 알고 있음
  - 이 값은 도시마다 다르며, 액수는 고정
  - 도시를 방문할 때마다 그 돈을 벌게 됨
 4. 버는 돈보다 쓰는 돈이 많다면, 도착 도시에 도착할 때 가진 돈의 액수가 음수가 될 수 있음
 5. 같은 도시를 여러 번 방문 가능, 방문할 때 마다 돈을 벌게 됨
 6. 모든 교통 수단은 입력으로 주어진 방향으로만 이용 가능하며 여러 번 이용 가능
[입력]
 1. N: 도시의 수, S: 시작 도시, E: 도착 도시, M: 교통 수단의 개수
 2. M개의 줄: 교통수단의 정보(시작, 끝, 가격)
 3. 마지막 줄: 각 도시에서 벌 수 있는 돈의 최댓값이 0번 도시부터 차례대로 주어짐
[출력]
 1. 도착 도시에 도착할 때 가지고 있는 돈의 액수의 최댓값 출력
   (도착 도시에 도착하는 것이 불가능할 때는 'gg', 돈을 무한히 가질 수 있다면 'Gee' 출력)
"""

"""
<풀이>
 1. 벨만 포드
 2. 양수 값으로 고려 해야하고, 버는 돈을 생각하기
 3. 싸이클이 발생한 지점에서 도착지점에 도달할 수 있는지 확인하기(출발지 시작)
"""
from collections import deque


def bellman_ford(transportations, earnings):
    # 최단 거리 리스트 및 처음에 가지고 있는 돈
    distances = [-10e9] * N
    distances[S] = earnings[S]

    # N 라운드 반복
    for i in range(1, N + 1):
        # M 번의 교통수단 이용
        for j in range(M):
            # 현재 지역, 다음 지역, 비용
            now = transportations[j][0]
            new = transportations[j][1]
            expense = transportations[j][2]

            # 현재 지점에 방문하지 않았다면
            if distances[now] != -10e9:
                # 값 갱신하기
                if distances[new] < distances[now] + earnings[new] - expense:
                    distances[new] = distances[now] + earnings[new] - expense

                    # N번째(마지막) 라운드에서도 갱신이 된다면 순환이 발생한 것
                    if i == N:
                        # 사이클이 생기는 지점에서 도착지로 갈 수 있는지 확인
                        if bfs(now, cities):
                            return 'Gee'

    # 방문하지 않았다면 gg
    if distances[E] == -10e9:
        return 'gg'
    # 방문했다면 도착 지역에서 최대로 벌 수 있는 돈
    else:
        return distances[E]


# 싸이클 출발지에서 도착지 방문 확인
def bfs(departures, cities):
    q = deque([departures])
    visited = [0] * N
    visited[departures] = 1

    while q:
        now = q.popleft()

        # 도착지에 도달했다면 True
        if now == E:
            return True

        for new in cities[now]:
            if not visited[new]:
                visited[new] = 1
                q.append(new)

    # 도착지에 도달하지 못한 경우
    return False


N, S, E, M = map(int, input().split())
# 모든 교통수단
transportations = []
cities = [[] for _ in range(N)]
for _ in range(M):
    start, end, fee = map(int, input().split())
    transportations.append((start, end, fee))
    cities[start].append(end)
# 각 도시에서 벌 수 있는 돈의 최댓값
earnings = list(map(int, input().split()))

print(bellman_ford(transportations, earnings))