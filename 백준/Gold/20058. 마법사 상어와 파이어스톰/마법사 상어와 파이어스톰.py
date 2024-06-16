import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마법사 상어와 파이어스톰 (20058)
 1. 파이어스톰은 먼저 격자를 2^L x 2^L 크기의 부분 격자로 나눔
 2. 그 후 모든 부분 격자를 시계 방향으로 90도 회전
 3. 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음 양 1 감소
 4. 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면 두 칸은 연결되어 있음
 5. 덩어리 = 연결된 칸의 집합
[입력]
 1. N: 격자 크기, Q: 파이어스톰 횟수
 2. 2^N개의 줄: 격자 정보
 3. 마지막 줄: 파이어스톰 단계
[출력]
 1. 남아있는 얼음 양의 합
 2. 가장 큰 덩어리가 차지하는 칸의 개수(덩어리가 없으면 0 출력)
"""

"""
<풀이>
 1. 일단 풀어보기
"""
from collections import deque


# 파이어 스톰
def fire_storm(L, arr):
    # 격자 복사
    arr_copy = [a[:] for a in arr]

    # 격자 나누기
    for x in range(0, 2 ** N, 2 ** L):
        for y in range(0, 2 ** N, 2 ** L):

            # 90도 회전 (90도 회전될 turn_y, turn_x 인덱스 조정)
            turn_y = y + (2 ** L) - 1
            for ori_x in range(x, x + (2 ** L)):
                turn_x = x
                for ori_y in range(y, y + (2 ** L)):
                    arr_copy[turn_x][turn_y] = arr[ori_x][ori_y]
                    # x축 증가
                    turn_x += 1
                # y축 감소
                turn_y -= 1

    # 격자 교체
    arr = [a[:] for a in arr_copy]

    # 얼음 녹이기
    for x in range(2 ** N):
        for y in range(2 ** N):
            # 얼음이 있는 공간이라면
            if arr[x][y]:
                cnt = 0
                # 델타 탐색
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    # 벽 형성
                    if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N:
                        # 얼음이 없는 공간이라면 cnt 추가
                        if arr[nx][ny] == 0:
                            cnt += 1
                    # 벽쪽이라면 얼음이 없는 것
                    else:
                        cnt += 1

                    # 얼음이 없는 공간이 2개 이상이라면 녹이고 종료
                    if cnt >= 2:
                        arr_copy[x][y] -= 1
                        break

    return arr_copy


# 얼음의 합 세기
def count_ice(arr):
    cnt = 0
    for x in range(2 ** N):
        cnt += sum(arr[x])

    return cnt


# 가장 큰 덩어리가 차지하는 칸의 개수 찾기 -> bfs
def count_lump(arr):
    max_cnt = 0
    visited = [[0] * (2 ** N) for _ in range(2 ** N)]

    for x in range(2 ** N):
        for y in range(2 ** N):
            # 얼음이 있는 공간이고 방문하지 않았다면
            if arr[x][y] and not visited[x][y]:
                visited[x][y] = 1
                q = deque([(x, y)])
                cnt = 1

                while q:
                    sx, sy = q.popleft()
                    # 델타 탐색
                    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        nx, ny = sx + dx, sy + dy
                        # 벽 형성 및 방문하지 않은 곳이라면
                        if 0 <= nx < 2 ** N and 0 <= ny < 2 ** N and not visited[nx][ny]:
                            # 얼음과 연결되어 인큐
                            if arr[nx][ny]:
                                cnt += 1
                                q.append((nx, ny))
                                visited[nx][ny] = 1

                max_cnt = max(max_cnt, cnt)

    return max_cnt


N, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2 ** N)]
level = list(map(int, input().split()))

# 파이어 스톰 진행
for i in range(Q):
    # 격자 바꾸기
    arr = fire_storm(level[i], arr)

print(count_ice(arr))
print(count_lump(arr))