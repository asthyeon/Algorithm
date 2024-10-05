import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 너구리 구구 (18126)
 1. 모든 방은 1~N번 번호 존재
 2. 입구는 1번
 3. 아이스크림을 입구에서 최대한 먼 방에 숨기려고 함
[입력]
 1. N: 방의 수
 2. N-1개의 줄: A번 방과 B번 방 사이를 양방향으로 연결하는 길의 길이가 C
[출력]
 1. 구구가 집 입구에서 아이스크림을 숨기려고 하는 방까지 이동하는 거리 구하기
"""

"""
<풀이>
 1. bfs
"""


def bfs(rooms):
    visited = [0] * (N + 1)
    q = [(0, 1)]
    visited[1] = 1
    answer = 0

    while q:
        now_dist, now = q.pop()
        
        # 정답 갱신
        answer = max(answer, now_dist)
        
        # 새로운 방 탐색
        for new_dist, new in rooms[now]:
            if not visited[new]:
                visited[new] = 1
                q.append((now_dist + new_dist, new))

    return answer


N = int(input())
# 방 정보
rooms = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())

    rooms[A].append((C, B))
    rooms[B].append((C, A))
# 각 방 오름차순 정렬
for room in rooms:
    room.sort()

print(bfs(rooms))