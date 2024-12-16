import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 점프 게임
 1. 가장 처음 왼쪽 줄 1번 칸 위에서 시작
 2. 3가지 행동 가능
  - 한 칸 앞 이동(i -> i+1)
  - 한 칸 뒤 이동(i -> i-1)
  - 반대편 줄로 점프, 원래 있던 칸보다 k칸 앞의 칸으로 이동(i -> i+k)
 3. N번 칸 보다 더 큰 칸으로 이동하는 경우 게임 클리어
 4. 1초에 한 칸씩 각 줄의 첫 칸이 사라짐(유저 이동 후, 칸이 사라짐)
[입력]
 1. N: 칸 수, k: 반대편 줄로 이동할 때 뛰어야 하는 칸 수
 2. 왼쪽 줄 정보: 0: 위험한 칸, 1: 안전한 칸
 3. 오른쪽 줄 정보: 0: 위험한 칸, 1: 안전한 칸
[출력]
 1. 게임을 클리어할 수 있으면 1, 없으면 0
"""

"""
<풀이>
 1. bfs
 2. 뒤에서 사라진 발판에는 갈 수 없음
"""
from collections import deque


def bfs(lines):
    q = deque([(0, 0, 0)])
    visited = [[0] * N for _ in range(2)]
    visited[0][0] = 1

    while q:
        cnt, x, y = q.popleft()

        if x == 1:
            # 탐색(반대편, 앞, 뒤)
            for dx, dy in [(-1, K), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # 범위 안에 안전한 곳에 방문하지 않았을 때
                if (0 <= nx < 2 and 0 <= ny < N and
                    lines[nx][ny] == '1' and not visited[nx][ny]
                    and ny > cnt):
                    # 시간을 늘려가며 방문
                    q.append((cnt + 1, nx, ny))
                    visited[nx][ny] = 1
                # 게임 클리어
                elif ny >= N and cnt <= N:
                    return 1
        else:
            # 탐색(반대편, 앞, 뒤)
            for dx, dy in [(1, K), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                # 범위 안에 안전한 곳에 방문하지 않았을 때
                if (0 <= nx < 2 and 0 <= ny < N and
                    lines[nx][ny] == '1' and not visited[nx][ny]
                    and ny > cnt):
                    # 시간을 늘려가며 방문
                    q.append((cnt + 1, nx, ny))
                    visited[nx][ny] = 1
                # 게임 클리어
                elif ny >= N and cnt <= N:
                    return 1

    # 클리어 실패
    return 0


N, K = map(int, input().split())
left = list(input().rstrip())
right = list(input().rstrip())

lines = [left, right]
print(bfs(lines))