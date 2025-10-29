import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 게임 (1072)
1. X: 게임 횟수, Y: 이긴 게임, Z: 승률
2. 앞으로의 모든 게임에서 지지 않음
3. X와 Y가 주어졌을 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지?
 - Z가 절대 변하지 않는다면 -1 출력
<풀이>
1. 브루트포스 -> 시간초과일 확률 높음(최대 10억번 연산)
2. 이분탐색
 - 예외: 승률 100% -> 변하지 않음, 승률 99% -> 승률이 100%가 될 수 없음
3. 소수점 유의 -> middle을 int화
 - y * 100으로 소수점 오차 해결하기
"""


def binary_search(X, Y, Z):
    # 최소 횟수부터 최대 횟수 설정
    start = 1
    end = 1000000000
    answer = 1

    while start <= end:
        middle = int((start + end) // 2)

        # 값이 더 크다면 답을 교체 후, 범위 줄이기
        if Z < int((Y + middle) * 100 / (X + middle)):
            answer = middle
            end = middle - 1
        # 값이 더 작다면 범위 늘리기
        else:
            start = middle + 1

    return answer


X, Y = map(int, input().split())
Z = int(Y * 100 / X)

# 예외 케이스
if Z == 99 or Z == 100:
    print(-1)
# 이분 탐색
else:
    print(binary_search(X, Y, Z))