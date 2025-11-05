import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 숨바꼭질 2 (12851)
1. 수빈이의 위치가 X일 때 1초 후에
 - X - 1, X + 1, 2 * X 위치로 이동
2. 동생을 찾는 가장 빠른 시간?
<풀이>
1. bfs
2. 가장 빠른 시간으로 찾는 방법의 수도 찾아야 함 -> 방문 기록 X -> 메모리 초과
3. 방문 기록을 시간으로 하기 -> 방문했던 지점이라면 최단 시간인지 확인
4. 동생을 찾았을 때는 탐색 중지
"""
from collections import deque


def bfs(start, target):
    # 시작 초기화
    INF = 100001
    visited = [0] * INF
    q = deque([(0, start)])
    # 가장 빠른 시간, 가장 빠른 시간의 방법의 수
    fastest = 0
    cnt = 0

    while q:
        time, now = q.popleft()

        # 조건 만족시 가장 빠른 시간 체크 및 카운트
        if now == target:
            fastest = time
            cnt += 1
            # target을 찾았기 때문에 이번 탐색 중지
            continue

        # 다음 장소 탐색
        if 0 <= now + 1 < INF:
            if not visited[now + 1] or visited[now + 1] == time + 1:
                visited[now + 1] = time + 1
                q.append((time + 1, now + 1))
        if 0 <= now - 1 < INF:
            if not visited[now - 1] or visited[now - 1] == time + 1:
                visited[now - 1] = time + 1
                q.append((time + 1, now - 1))
        if 0 <= 2 * now < INF:
            if not visited[2 * now] or visited[2 * now] == time + 1:
                visited[2 * now] = time + 1
                q.append((time + 1, 2 * now))

    print(fastest)
    print(cnt)


# N: 수빈 위치, K: 동생 위치
N, K = map(int, input().split())

bfs(N, K)