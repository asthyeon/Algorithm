import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 랭킹전 대기열 (20006)
 1. 매칭 시스템
  - 플레이어가 입장 신청시 가능한 방이 없다면 새로운 방 생성 및 입장
  - 해당 방에는 처음 입장 플레이어 레벨 기준 +- 10
  - 입장 가능한 방이 있다면 입장시킨 후 정원이 찰 때까지 대기
  - 입장이 가능한 방이 여러 개라면 먼저 생성된 방 입장
  - 방 정원이 차면 게임 시작
[입력]
 1. p: 플레이어 수, m: 방 정원
 2. p개의 줄: l: 레벨, n: 닉네임
[출력]
 1. 모든 방에 대해 게임 시작 유무와 방에 있는 플레이어 레벨과 아이디 출력
 2. 플레이어 정보는 닉네임 사전순, 시작: Started!, 대기 중: Waiting!
"""

"""
<풀이>
 1. 딕셔너리 이용
"""

p, m = map(int, input().split())
# 방 정보와 방 순서, 생성된 방 번호, 비어있는 방 순서
rooms = {}
room_level = [0]
room_number = 1
for _ in range(p):
    l, n = input().split()
    l = int(l)

    # 첫 생성시
    if len(room_level) == 1:
        room_level.append(l)
        rooms[room_number] = [(n, l)]

    # 그 외
    else:
        # 방 채우기
        for lev in range(1, room_number + 1):
            # 이번 방 정원이 안찼다면
            if len(rooms[lev]) < m:
                # 조건 만족시
                if room_level[lev] - 10 <= l <= room_level[lev] + 10:
                    rooms[lev].append((n, l))
                    break
        # 정원이 다 차있거나 조건을 만족하는 방이 없다면
        else:
            # 새로운 방 생성
            room_number += 1
            room_level.append(l)
            rooms[room_number] = [(n, l)]

# 정답 출력
for i in range(1, room_number + 1):
    # 시작 or 대기
    if len(rooms[i]) == m:
        print('Started!')
    else:
        print('Waiting!')

    # 사전순 정렬
    rooms[i].sort()

    # 플레이어 정보 출력
    for nick, level in rooms[i]:
        print(level, nick)


