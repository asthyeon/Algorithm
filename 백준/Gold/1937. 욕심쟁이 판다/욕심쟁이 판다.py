import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 욕심쟁이 판다 (1937)
 1. 판다는 대나무를 다 먹으면 상하좌우중 전 지역보다 대나무가 많은 곳으로 이동
 2. 처음 시작 지점을 어떤 곳으로 해야 최대한 많은 칸을 방문할 수 있는지 파악하기
[입력]
 1. n: 대나무 숲의 크기
 2. n개의 줄: 대나무 숲의 정보
[출력]
 1. 판다가 이동할 수 있는 칸의 수의 최댓값 출력
"""

"""
<풀이>
 1. bfs -> 메모리 초과
 2. dfs + dp
"""
sys.setrecursionlimit(10 ** 9)


# dfs
def dfs(x, y, forest, dp):
    # 방문한 곳이라면 종료
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1

    # 델타탐색
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        # 벽 생성 및 조건이 맞다면
        if 0 <= nx < N and 0 <= ny < N and forest[x][y] < forest[nx][ny]:
            # 재귀
            dp[x][y] = max(dp[x][y], dfs(nx, ny, forest, dp) + 1)

    return dp[x][y]


N = int(input())
forest = [list(map(int, input().split())) for _ in range(N)]

# 정답 및 dp 배열
answer = 1
dp = [[0] * N for _ in range(N)]

for x in range(N):
    for y in range(N):
        # 정답 갱신
        answer = max(answer, dfs(x, y, forest, dp))

print(answer)