import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# Puyo Puyo(11559)
 1. 뿌요뿌요 룰
  ㄱ. 실제 뿌요뿌요와 유사
  ㄴ. 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 뿌요 없어짐(1연쇄)
  ㄷ. 없어진 부분을 다시 위의 뿌요들이 채워넣음
  ㄹ. ㄴ 반복(터질 때 동시에 여러 그룹이 터질 수도 있지만 연쇄는 1연쇄로 처리)
 2. 연쇄가 몇 번 연속으로 일어날지 계산하기
[입력]
 1. 총 12개의 줄로 각 줄에는 6개의 문자가 필드 정보가 주어짐
 2. .: 빈공간, R: 빨강, G: 초록, B: 파랑, P: 보라, Y: 노랑
[출력]
 1. 몇 연쇄가 되는지 출력
 2. 하나도 터지지 않으면 0 출력
"""

"""
<풀이>
 1. 연쇄를 한번의 체크과정으로 보기
 2. bfs
"""
from copy import deepcopy


# 뿌요뿌요
def puyopuyo(field):
    # 연쇄횟수
    chain = 0

    while True:
        # 필드 복사
        field_copy = deepcopy(field)
        # 방문 리스트
        visited = [[0] * 6 for _ in range(12)]

        # 필드 탐색
        for sx in range(11, -1, -1):
            for sy in range(6):
                # 방문하지 않은 색깔이라면 bfs 탐색
                if not visited[sx][sy] and field[sx][sy] != '.':

                    # 탐색용 큐
                    q = [(sx, sy)]
                    # 터트릴 리스트
                    bombs = [(sx, sy)]
                    while q:
                        x, y = q.pop()
                        visited[x][y] = 1
                        # 델타탐색
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            # 벽 생성 및 같은 색이라면 cnt 추가 및 인큐
                            if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny]:
                                if field[nx][ny] == field[sx][sy]:
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))
                                    bombs.append((nx, ny))
                    # 터트릴 뿌요가 4개 이상이라면 터뜨리기
                    if len(bombs) >= 4:
                        for x, y in bombs:
                            field_copy[x][y] = '.'

        # 뿌요들 정렬
        for y in range(6):
            for x in range(11, -1, -1):
                # 빈 칸이라면 다른 색상 탐색한 후 끌어오기
                if field_copy[x][y] == '.':
                    for sx in range(x - 1, -1, -1):
                        if field_copy[sx][y] != '.':
                            field_copy[x][y] = field_copy[sx][y]
                            field_copy[sx][y] = '.'
                            break

        # 연쇄가 발생했다면 연쇄 추가 및 필드 교체
        if field_copy != field:
            chain += 1
            field = field_copy
        # 연쇄가 멈췄다면 연쇄 반환
        else:
            return chain


# 필드 정보
field = [list(input().rstrip()) for _ in range(12)]

print(puyopuyo(field))