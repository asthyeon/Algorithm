import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 바이러스 (2606)
1. bfs
"""
from collections import deque


def bfs(network):
    # 감염된 컴퓨터, 1번 감염 처리
    infected = [0] * (N + 1)
    infected[1] = 1
    q = deque([1])
    
    cnt = 0
    while q:
        # 현재 컴퓨터
        now = q.pop()
        # 새로운 컴퓨터 탐색 및 감염
        for new in network[now]:
            if not infected[new]:
                q.append(new)
                infected[new] = 1
                cnt += 1

    return cnt


# 컴퓨터 수, 연결된 컴퓨터 쌍의 수
N = int(input())
V = int(input())
# 연결된 네트워크
network = [[] for _ in range(N + 1)]
for _ in range(V):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

print(bfs(network))