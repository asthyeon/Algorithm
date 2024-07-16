import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 전단지 돌리기 (19542)
 1. 트리 모양 길에서 모든 노드에 전단지를 돌리고 출발지로 돌아오기
 2. 현재 노드에서 거리가 D 이하인 모든 노드에 전단지를 돌릴 수 있음
[입력]
 1. N: 노드의 개수, S: 케니소프트의 위치, D: 힘
 2. N-1개의 줄: 트리의 간선 정보: x번 노드와 y번 노드가 연결되어 있음
 3. 모든 간선의 길이는 1
[출력]
 1. 목표를 완수하기 위해 이동해야 하는 최소 거리 출력
"""

"""
<풀이>
 1. dfs
"""
sys.setrecursionlimit(10 ** 9)


# dfs
def dfs(now, before):
    global minimum
    # 지나온 거리
    distance = 0
    # 새로운 위치 탐색
    for new in tree[now]:
        # 새로운 위치가 이전 위치와 다를 경우
        if new != before:
            # 지나온 거리 갱신
            distance = max(distance, dfs(new, now))
    # 지나온 거리가 D 보다 클 경우 최소 거리 + 1
    if distance >= D:
        minimum += 1
    # 거리 증가
    return distance + 1


N, S, D = map(int, input().split())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

# 최소 거리
minimum = 0
# dfs 탐색 (현재 위치, 이전 위치)
dfs(S, 0)

# 최소 거리가 0보다 클 경우 왕복
if minimum > 0:
    print((minimum - 1) * 2)
# 최소 거리가 0일 경우
else:
    print(0)