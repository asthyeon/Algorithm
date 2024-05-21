import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 도시 분할 계획 (1647)
 1. 임의의 두 집 사이에 경로 항상 존재(양방향)
 2. 마을을 분할할 때 분리된 마을 안에 집들이 서로 연결되도록 분할
 3. 마을에는 집이 하나 이상 있어야 함
 4. 두 마을 사이 길을 없앨 수 있음
 5. 분리된 마을 안에서도 길을 더 없앨 수 있음
[입력]
 1. N: 집의 개수, M: 길의 개수
 2. M개의 줄: A번 집과 B번 집을 연결하는 길의 유지비 C
[출력]
 1. 없애고 남은 길 유지비의 합의 최솟값
"""

"""
<풀이>
 1. 일단 풀어보기 -> MST
 2. MST로 연결된 길 중 유지비가 가장 큰 길만 없애기
"""
import heapq


# 프림
def prim(arr):
    # 방문 리스트
    visited = [0] * (N + 1)
    # 시작 유지비, 시작점
    hq = [(0, 1)]
    # 총 비용
    total = 0
    # 가장 큰 값
    maximum = 0

    while hq:
        cost, now = heapq.heappop(hq)
        
        # 방문하지 않았다면 방문
        if not visited[now]:
            total += cost
            visited[now] = 1
            maximum = max(maximum, cost)
                
            # 방문하지 않은 곳만 인큐
            for new in arr[now]:
                if not visited[new[1]]:
                    heapq.heappush(hq, (new[0], new[1]))

    return total - maximum


N, M = map(int, input().split())
arr = [[] for _ in range(N + 1)]

# 간선 연결
for _ in range(M):
    A, B, C = map(int, input().split())
    arr[A].append((C, B))
    arr[B].append((C, A))

print(prim(arr))