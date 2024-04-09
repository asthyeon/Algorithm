import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 네트워크 복구 (2211)
 1. 컴퓨터들이 직접 연결 회선 or 간접적으로 통신 가능
 2. 최소 개수의 회선만 복구하여 네트워크 복구하기
 3. 슈퍼컴퓨터가 통신하는 시간 보다 길어져서는 안됨
[입력]
 1. N: 컴퓨터의 수, M: 회선의 수
 2. M개의 줄: A번 과 B번이 통신 시간 C인 회선으로 연결됨
 3. 1번 컴퓨터는 보안 시스템을 설치할 슈퍼 컴퓨터
 4. 쌍방향
[출력]
 1. 복구할 회선의 개수 K 출력
 2. K개의 줄에 복구한 회선을 나타내는 두 정수 A, B 출력
 3. 출력은 임의의 순서대로 가능하며, 답이 여러 개 존재할 시 아무 것이나 하나 출력
"""

"""
<풀이>
 1. 다익스트라 -> MST
 2. 각 회선이 어디에 연결되어 있는지 갱신하기
"""
import heapq
INF = 10e9


# 다익스트라
def dijkstra(network):
    hq = [(0, 1)]
    distances = [INF] * (N + 1)
    distances[1] = 0

    # 연결된 회선들 정보
    connections = [i for i in range(N + 1)]

    while hq:
        dist, now = heapq.heappop(hq)

        for new_dist, new in network[now]:
            new_dist = new_dist + dist

            if distances[new] > new_dist:
                heapq.heappush(hq, (new_dist, new))
                distances[new] = new_dist
                # 연결 회선 갱신
                connections[new] = now

    # MST
    print(N - 1)
    for connection in range(2, N + 1):
        print(connection, connections[connection])


N, M = map(int, input().split())
# 네트워크 정보
network = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())

    network[A].append((C, B))
    network[B].append((C, A))

dijkstra(network)

