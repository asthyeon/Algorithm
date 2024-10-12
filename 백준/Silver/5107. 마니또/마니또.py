import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마니또 (5107)
 1. 마니또 체인
  - 누군가는 처음 선행을 베푼 사람에게 선행을 베풀게 됨
[입력]
 1. N: 사람 수(N = 0이면 입력의 끝)
 2. N개의 줄: 선행을 베푸는 사람, 선행을 받는 사람
[출력]
 1. 해당 케이스의 번호와 연결 고리의 개수를 공백을 두고 출력
"""

"""
<풀이>
 1. MST
"""
from collections import deque


# MST
def MST(start, visited):
    global cnt
    q = deque([start])
    visited[start] = 1

    while q:
        now = q.popleft()

        # 방문하지 않은 장소라면 탐색
        for new in people[now]:
            # 방문 처리
            if not visited[new]:
                q.append(new)
                visited[new] = 1

            # 시작 지점으로 돌아왔다면 종료
            if new == start:
                cnt += 1
                return


# 테스트 케이스 번호
case = 1
while True:
    N = int(input())

    if N == 0:
        break

    # 사람에게 부여될 각 번호와 리스트
    number = 0
    people = [[] for _ in range(N)]
    matching = {}

    for _ in range(N):
        giver, taker = map(str, input().split())

        # 번호가 부여된 사람이 아니라면 번호 부여
        if giver not in matching:
            matching[giver] = number
            number += 1

        if taker not in matching:
            matching[taker] = number
            number += 1

        people[matching[giver]].append(matching[taker])

    # 방문 리스트와 연결 고리 수
    visited = [0] * N
    cnt = 0

    for start in range(N):
        if not visited[start]:
            MST(start, visited)

    print(case, cnt)
    case += 1