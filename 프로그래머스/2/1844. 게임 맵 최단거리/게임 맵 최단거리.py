"""
[문제] 게임 맵 최단거리
1. 상대 팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값 return
2. 도착할 수 없을 때는 -1 return
3: 0: 벽, 1: 벽이 없는 자리

[풀이]
1. bfs
"""
from collections import deque


def solution(maps):
    # R(세로), C(가로) 측정
    R = len(maps)
    C = len(maps[0])
    
    
    def bfs(maps, R, C):
        # 방문 리스트 초기화 및 시작점 방문
        visited = [[0] * C for _ in range(R)]
        q = deque([(0, 0)])
        visited[0][0] = 1
        
        while q:
            x, y = q.popleft()
            
            # 델타 탐색
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    # 다음 지역이 방문하지 않았고 벽이 없는 자리라면
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        # 칸 수 + 1 및 다음 좌표 인큐
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
        
        return visited[R - 1][C - 1]
        
    answer = bfs(maps, R, C)
    # 방문할 수 없다면 -1 출력
    if answer == 0:
        return -1
    return answer