"""
# 경주로 건설
 1. N x N 크기의 경주로 부지
  - 0: 칸이 비어 있음, 1: 칸이 벽으로 채워져 있음
  - 출발점(0, 0) -> 도착점(N - 1, N - 1)
  - 상, 하, 좌, 우로 인접한 두 빈 칸을 연결하여 경주로 건설 가능
 2. 인접한 두 빈 칸을 상하 or 좌우로 연결: 직선 도로(100원 소요)
 3. 두 직선 도로가 서로 직각으로 만나는 지점: 코너(500원 소요)
 4. 항상 출발점 ~ 도착점까지 건설 가능
 4. 경주로를 건설하는데 필요한 최소 비용 계산
[입력]
 1. 2차원 정사각 배열 board
[출력]
 1. 경주로를 건설하는데 필요한 최소 비용 return
"""

"""
<풀이>
 1. 다익스트라 이용
"""
import heapq
# 최댓값
INF = 10e9
# 방향
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 방향 역참조
back_refs = {
    (0, 1): 0,
    (1, 0): 1,
    (0, -1): 2,
    (-1, 0): 3,
}


def solution(board):
    # 다익스트라
    def dijkstra(board):
        # 최소비용, x좌표, y좌표, 방향 인큐
        hq = [(0, 0, 0, -1)]
        # 부지 크기 N
        N = len(board)
        # 방문배열(각 거리마다의 최소비용, 3차원 배열로 만들어서 각 방향별로 저장하기)
        visited = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

        while hq:
            cost, x, y, direction = heapq.heappop(hq)
            
            # 델타탐색
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                # 벽형성
                if 0 <= nx < N and 0 <= ny < N:
                    # 벽이 아니라면
                    if board[x][y] == 0:
                        
                        # 출발점일 때는 직선 도로
                        if direction == -1:
                            new_cost = cost + 100

                            # 다음 지점에 직선 도로 건설 및 각 방향별 인큐
                            visited[nx][ny][back_refs[(dx, dy)]] = new_cost
                            heapq.heappush(hq, (new_cost, nx, ny, back_refs[(dx, dy)]))
                        
                        # 출발점 외
                        else:
                            # 방향에 따라 비용 산정
                            # 같은 방향에서 오면 직선도로
                            if direction == back_refs[(dx, dy)]:
                                new_cost = cost + 100
                            # 다른 방향에서 오면 직선도로 + 코너
                            else:
                                new_cost = cost + 600
                                
                            # 다음 장소에 산정된 비용보다 저렴할 때만 방문
                            if visited[nx][ny][back_refs[(dx, dy)]] >= new_cost:
                                visited[nx][ny][back_refs[(dx, dy)]] = new_cost
                                heapq.heappush(hq, (new_cost, nx, ny, back_refs[(dx, dy)]))
    
        
        return min(visited[N - 1][N - 1])
    
        
    return dijkstra(board)