import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 인내의 도미노 장인 호석(20165)
 1. 게임 룰
  ㄱ. N 행 M 열의 2차원 격자 모양의 게임판의 각 격자에 1 이상 5 이하 높이 도미노 세움
  ㄴ. 매 라운드 공격수 먼저 공격, 수비수는 공격 끝난 후에 수비
  ㄷ. 공격수는 도미노를 동, 서, 남, 북 중 원하는 방향으로 넘어뜨림
  ㄹ. 길이가 k인 도미노가 특정 방향으로 넘어지면 k-1개의 도미노들이 같이 넘어짐(연쇄 가능)
  ㅁ. 넘어진 도미노가 있는 칸으로 공격한 경우 아무 일이 일어나지 않음
  ㅂ. 수비수는 넘어져 있는 도미노 중 하나를 세울 수 있음
  ㅅ. R 번의 라운드 동안 ㄷ, ㄹ 반복, 공격수는 해당 라운드에 넘어뜨린 도미노의 개수가 점수
 2. 선공으로 시작, 공격수의 점수와 게임판의 최종 상태 출력
[입력]
 1. N: 행 개수, M: 열 개수, R: 라운드 횟수
 2. N개의 줄: 게임판의 상태
 3. R x 2개의 줄: 각 라운드는 두 줄, 첫 줄은 공격수 두번째 줄은 수비수
 4. X Y D: 공격수가 X행 Y열의 도미노를 D 방향으로 밀어버림
 5. X Y: 수비수가 X행 Y열의 도미노를 다시 세움
 6. 이미 넘어진 걸 건드리면 아무 일도 일어나지 않음
[출력]
 1. 첫 줄에 공격수의 점수
 2. 게임판의 상태를 N줄에 걸쳐서 출력(F: 넘어진 것, S: 넘어지지 않은 것)
"""

"""
<풀이>
 1. 큐 이용 -> 인덱스 에러 뜸 이유는 모르겠다
 2. 그냥 구현해보기, 사실 큐 필요 없긴 함
"""
# 방향
directions = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}


# 라운드 진행
def play(domino):
    global attack
    # 넘어져 있는 도미노라면 공격자는 종료 후 수비자만 행동
    if domino[a_x][a_y] == 0:
        # 넘어진 도미노라면 세우기
        if domino[d_x][d_y] == 0:
            domino[d_x][d_y] = domino_copy[d_x][d_y]
            return

    # 높이 저장 및 초기화 및 공격로 점수 세기
    height = domino[a_x][a_y]
    domino[a_x][a_y] = 0
    attack += 1
    # 방향 저장
    dx, dy = directions[a_d]
    x, y = a_x, a_y
    # 공격자 도미노 무너뜨리기
    while height - 1:
        x, y = x + dx, y + dy
        # 높이 깎기
        height -= 1
        # 벽형성
        if 0 <= x < N and 0 <= y < M:
            # 현재 높이가 더 높다면 교체
            if height < domino[x][y]:
                height = domino[x][y]
                domino[x][y] = 0
                attack += 1
            # 현재 높이가 0이라면 넘기기
            elif domino[x][y] == 0:
                continue
            # 현재 높이가 더 낮다면 쓰러뜨리기
            else:
                domino[x][y] = 0
                attack += 1
        # 벽 범위를 벗어나면 종료
        else:
            break

    # 수비자 행동 넘어진 도미노라면 세우기
    if domino[d_x][d_y] == 0:
        domino[d_x][d_y] = domino_copy[d_x][d_y]


# 도미노 판 점검
def check(domino):
    # 공격수 점수 출력
    print(attack)

    # 도미노 판 영어로 변환 후 출력
    for x in range(N):
        for y in range(M):
            if domino[x][y] == 0:
                domino[x][y] = 'F'
            else:
                domino[x][y] = 'S'

    for i in range(N):
        print(*domino[i])


# 크기 N, M 라운드 횟수 R
N, M, R = map(int, input().split())
# 도미노 판
domino =[list(map(int, input().split())) for _ in range(N)]
# 공격수 점수
attack = 0
# 점수체크용 도미노 판 복사
domino_copy = [d[:] for d in domino[:]]
# 라운드 정보
for _ in range(R):
    # 공격자
    a_x, a_y, a_d = map(str, input().split())
    a_x, a_y = int(a_x) - 1, int(a_y) - 1
    # 수비자
    d_x, d_y = map(int, input().split())
    d_x -= 1
    d_y -= 1

    # 라운드 진행
    play(domino)

# 최종 결과 출력
check(domino)