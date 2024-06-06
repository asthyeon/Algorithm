import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주사위 놓기 (2116)
 1. 주사위를 쌓을 때 서로 붙어 있는 두 개의 주사위에서
  - 아래에 있는 주사위의 윗면에 적혀있는 숫자 = 위에 있는 주사위의 아랫면에 적혀있는 숫자
  - 1번 주사위는 마음대로 놓을 수 있음
 2. 각 주사위를 위 아래로 고정한 채 옆으로 90, 180, 270도 돌릴 수 있음
[입력]
 1. 첫 줄: 주사위 개수
 2. 주사위 개수 만큼: 주사위의 전개도가 주어짐 A, B, C, D, E, F
[출력]
 1. 한 옆면의 숫자의 합이 가장 큰 값 출력
"""

"""
<풀이>
 1. 일단 풀어보기
 2. 미리 어느 면이 맞붙는지 생각하기
- A = F, B = D, C = E
- 0 = 5, 1 = 3, 2 = 4
 3. 1번 주사위를 놓는 6가지의 경우 생각하기
"""
# 맞붙는 면
attach = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}


# 주사위 쌓기
def stack(dices, turn, top):
    global maximum
    # 같은 숫자의 인덱스 찾기
    for same in range(6):
        # 인덱스를 찾았다면
        if dices[turn][same] == top:
            # 옆면 중 가장 큰 값 찾기
            side_maximum = 0
            for side in range(6):
                # 윗면과 아랫면 제외
                if side == same or side == attach[same]:
                    continue
                side_maximum = max(side_maximum, dices[turn][side])
            # 값 더하기
            maximum += side_maximum
            # 윗면 교체
            return dices[turn][attach[same]]


N = int(input())
dices = []
for _ in range(N):
    dice = list(map(int, input().split()))
    dices.append(dice)

# 최대 합
answer = 0
# 1번 주사위를 놓는 6가지 경우
for i in range(1, 7):
    # 이번 경우의 최대 합
    maximum = 0
    # 위로 놓는 면
    top = i

    # 주사위 쌓기
    for j in range(N):
        top = stack(dices, j, top)
    # 최대 합 교체
    answer = max(answer, maximum)

print(answer)

