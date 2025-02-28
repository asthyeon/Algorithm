import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 맥주 마시면서 걸어가기 (9205)
 1. 맥주 1병을 마시면 50미터 갈 수 있음
 2. 한 박스에는 맥주 20병, 편의점에서 한 박스 구매 가능
[입력]
 1. t: 테스트 케이스의 개수
 2. n: 맥주를 파는 편의점의 개수
 3. n+2개의 줄: 집, 편의점, 펜타포트 락 페스티벌 좌표
[출력]
 1. 페스티벌에 갈 수 있으면 "happy", 맥주가 바닥나서 이동 불가시 "sad" 출력
"""

"""
<풀이>
 1. bfs
"""
from collections import deque


def bfs(home, festival, convenience):
    visited = [0] * n
    q = deque([home])

    while q:
        x, y = q.popleft()

        # 페스티발 도착 가능할 시
        if abs(x - festival[0]) + abs(y - festival[1]) <= 1000:
            return 'happy'

        # 편의점 확인
        for j in range(n):
            nx, ny = convenience[j]
            # 아직 방문하지 않고, 방문할 수 있다면
            if not visited[j] and abs(x - nx) + abs(y - ny) <= 1000:
                # 방문 및 위치 갱신
                visited[j] = 1
                q.append((nx, ny))

    # 페스티벌에 도착하지 못한다면
    return 'sad'


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    convenience = []
    for i in range(n + 2):
        x, y = map(int, input().split())

        if i == 0:
            home = (x, y)
        elif i == n + 1:
            festival = (x, y)
        else:
            convenience.append((x, y))

    print(bfs(home, festival, convenience))