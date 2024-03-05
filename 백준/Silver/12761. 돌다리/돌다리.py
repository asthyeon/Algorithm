import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 돌다리(12761)
 1. 동규는 N번 돌, 주미는 M번 돌
 2. 동규가 다리를 건너는 법
  - 한 턴에 현 위치 +1 or -1
  - 스카이 콩콩 이용시 현 위치에서 A or B 만큼 좌우로 점프 가능
  - 순간적으로 힘을 모아 현 위치의 A배 or B배 만큼 이동 가능
 3. 최대한 주미 빨리 만나기
[입력]
 1. A, B: 스카이 콩콩의 힘, N: 동규 위치, M: 주미 위치
[출력]
 1. 최소 이동 횟수 출력
"""

"""
<풀이>
 1. bfs
 2. 덱 사용
"""
from collections import deque


# 다익스트라
def bfs(A, B, N, M):
    # 돌다리 만들기
    bridge = [0] * 100001

    # 큐 생성 및 횟수와 동규 위치 인큐
    q = deque([(0, N)])

    # 도착시 종료
    if N == M:
        return 0

    while q:
        # 현재거리 및 현재위치 디큐
        now_cnt, now_loc = q.popleft()

        # 단순이동
        if 0 <= now_loc - 1 <= 100000:
            if not bridge[now_loc - 1]:
                bridge[now_loc - 1] = now_cnt + 1
                q.append((now_cnt + 1, now_loc - 1))
                # 도착시 종료
                if now_loc - 1 == M:
                    return now_cnt + 1
        if 0 <= now_loc + 1 <= 100000:
            if not bridge[now_loc + 1]:
                bridge[now_loc + 1] = now_cnt + 1
                q.append((now_cnt + 1, now_loc + 1))
                # 도착시 종료
                if now_loc + 1 == M:
                    return now_cnt + 1

        # 스카이 콩콩 이동
        if 0 <= now_loc - A <= 100000:
            if not bridge[now_loc - A]:
                bridge[now_loc - A] = now_cnt + 1
                q.append((now_cnt + 1, now_loc - A))
                # 도착시 종료
                if now_loc - A == M:
                    return now_cnt + 1
        if 0 <= now_loc + A <= 100000:
            if not bridge[now_loc + A]:
                bridge[now_loc + A] = now_cnt + 1
                q.append((now_cnt + 1, now_loc + A))
                # 도착시 종료
                if now_loc + A == M:
                    return now_cnt + 1
        if 0 <= now_loc - B <= 100000:
            if not bridge[now_loc - B]:
                bridge[now_loc - B] = now_cnt + 1
                q.append((now_cnt + 1, now_loc - B))
                # 도착시 종료
                if now_loc - B == M:
                    return now_cnt + 1
        if 0 <= now_loc + B <= 100000:
            if not bridge[now_loc + B]:
                bridge[now_loc + B] = now_cnt + 1
                q.append((now_cnt + 1, now_loc + B))
                # 도착시 종료
                if now_loc + B == M:
                    return now_cnt + 1

        # 파워 이동
        if 0 <= now_loc * A <= 100000:
            if not bridge[now_loc * A]:
                bridge[now_loc * A] = now_cnt + 1
                q.append((now_cnt + 1, now_loc * A))
                # 도착시 종료
                if now_loc * A == M:
                    return now_cnt + 1
        if 0 <= now_loc * B <= 100000:
            if not bridge[now_loc * B]:
                bridge[now_loc * B] = now_cnt + 1
                q.append((now_cnt + 1, now_loc * B))
                # 도착시 종료
                if now_loc * B == M:
                    return now_cnt + 1


# 스카이 콩콩의 힘 A, B, 동규 위치 N, 주미 위치 M
A, B, N, M = map(int, input().split())

print(bfs(A, B, N, M))

