import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 계산 로봇 (22342)
 1. 각 로봇은 하나 이상의 입력 값, 하나의 저장 값과 출력 값을 가짐
 2. 제일 왼쪽 열의 로봇들부터 열 번호 순서대로, 같은 열의 로봇들은 동시에 동작
 3. 로봇들의 동작
  - 제일 왼쪽 열에 있는 로봇의 입력 값은 0 하나로 정함
  - 좌표 (i, j)의 로봇의 입력 값은 |i - a| <= j - b, b < j 인 모든 좌표 (a, b)에 있는 출력 값
  - 각 로봇은 자신의 입력 값들 중 최댓값을 자신의 저장 값으로 한다
  - 각 로봇은 자신의 저장 값에 자신의 가중치 D를 더 한 값을 자신의 출력 값으로 한다
[입력]
 1. M: 가로줄, N: 세로줄
 2. M개의 줄: 로봇들의 가중치
[출력]
 1. 로봇들의 저장 값 중 최댓값을 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(arr):
    # 저장값
    dp_save = [[0] * (N + 1) for _ in range(M + 2)]
    # 출력값
    dp_output = [[0] * (N + 1) for _ in range(M + 2)]
    # 최대 값
    maximum = 0

    # 첫 열의 출력 값은 자기 자신
    for x in range(1, M + 1):
        dp_output[x][1] = arr[x][1]

    # 열 순으로 순회
    for y in range(2, N + 1):
        for x in range(1, M + 1):
            # 저장 값 갱신(이전 3개 출력 값 중 최대 값)
            dp_save[x][y] = max(dp_output[x - 1][y - 1],
                                dp_output[x][y - 1],
                                dp_output[x + 1][y - 1])
            # 출력 값 갱신(저장값 + 자기 자신의 가중치)
            dp_output[x][y] = dp_save[x][y] + arr[x][y]
            # 저장 값 중 최대 값 갱신
            maximum = max(maximum, dp_save[x][y])

    return maximum


M, N = map(int, input().split())
# 인덱스를 조정한 배열 생성
arr = ([list([0] * (N + 1))] +
       [[0] + list(map(int, input().rstrip())) for _ in range(M)] +
       [list([0] * (N + 1))])

print(dynamic_programming(arr))
