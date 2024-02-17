import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 기차가 어둠을 헤치고 은하수를(15787)
 1. 기차는 20개의 좌석 존재
 2. 기차에 대한 명령
  ㄱ. 1 i x: i번째 기차에 x번째 좌석에 사람 태우기(이미 타있을 경우 행동 X)
  ㄴ. 2 i x: i번째 기차에 x번째 좌석에 사람 하차(아무도 없을 경우 행동 X)
  ㄷ. 3 i: i번째 기차에 승객들 모두 한칸씩 뒤로(20번째 승객은 하차)
  ㄹ. 4 i: i번째 기차에 승객들 모두 한칸씩 앞으로(1번째 승객은 하차)
 3. M번의 명령 후 1번째 기차부터 순서대로 은하수를 건넘
  ㄱ. 기차가 지나갈 때 승객이 앉은 상태를 목록에 기록
  ㄴ. 이미 목록에 존재하는 기록일 시 해당 기차는 못 건넘
[입력]
 1. N: 기차의 수, M: 명령의 수
 2. 2 ~ M + 1 번째 줄: 명령
[출력]
 1. 은하수를 건널 수 있는 기차의 수 출력
"""

"""
<풀이>
 1. 일단 풀어보기
"""

# 기차의 수 N, 명령의 수 M
N, M = map(int, input().split())
# 기차 생성
trains = []
for _ in range(N):
    trains.append([0] * 20)

# 명령 이행
for _ in range(M):
    command = list(map(int, input().split()))
    
    # 1번째 명령(비어있으면 태우기)
    if command[0] == 1:
        if not trains[command[1] - 1][command[2] - 1]:
            trains[command[1] - 1][command[2] - 1] = 1
    
    # 2번째 명령(타고있으면 하차)
    elif command[0] == 2:
        if trains[command[1] - 1][command[2] - 1]:
            trains[command[1] - 1][command[2] - 1] = 0
    
    # 3번째 명령(전부 뒤로 이동)
    elif command[0] == 3:
        # 앞에 사람이 있는지 여부 체크
        front = 0
        now = 0
        for j in range(20):
            if front:
                now = 1
                front = 0
            # 마지막 승객 하차
            if j == 19:
                if trains[command[1] - 1][j] == 1:
                    trains[command[1] - 1][j] = 0
            # 그 외 승객 뒤로 이동
            else:
                if trains[command[1] - 1][j] == 1:
                    trains[command[1] - 1][j] = 0
                    front = 1

            # 앞에 승객이 있었으면 이동
            if now:
                trains[command[1] - 1][j] = 1
                now = 0

    # 4번째 명령(전부 앞으로)
    else:
        # 뒤에 사람이 있는지 여부 체크
        back = 0
        now = 0
        for j in range(19, -1, -1):
            if back:
                now = 1
                back = 0
            # 처음 승객 하차
            if j == 0:
                if trains[command[1] - 1][j] == 1:
                    trains[command[1] - 1][j] = 0
            # 그 외 승객 앞으로 이동
            else:
                if trains[command[1] - 1][j] == 1:
                    trains[command[1] - 1][j] = 0
                    back = 1

            if now:
                trains[command[1] - 1][j] = 1
                now = 0

# 은하수 건너기
milky_way = set()
for _ in range(N):
    milky_way.add(tuple(trains[_]))

print(len(milky_way))