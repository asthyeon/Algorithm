import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 용돈 관리 (6236)
 1. N일 동안 M번만 통장에서 돈을 빼서 씀
 2. 인출한 K원으로 하루를 보낼 수 있으면 그대로 사용
 3. 모자라게 되면 남은 금액은 통장에 넣고 다시 K원 인출
 4. 정확히 M번을 맞추기 위해 남은 금액이 그날 사용할 금액보다 많더라도 다시 입출금 가능
[입력]
 1. N: 기간, M: 인출 횟수
 2. N개의 줄: i번째 날에 이용할 금액
[출력]
 1. 현우가 통장에서 인출해야 할 최소 금액 K
"""

"""
<풀이>
 1. 이분 탐색
"""


def binary_search(days):
    # 인출해야 되는 최소 값과 최대 값
    minimum = min(days)
    maximum = sum(days)
    # 인출해야할 최소 금액
    K = 0

    while minimum <= maximum:
        # 인출해야 될 중간 값
        middle = (minimum + maximum) // 2

        # 인출 횟수 및 현재 인출한 금액
        cnt = 1
        now = middle
        # 매일 소비하기
        for day in range(N):
            # 현재 돈이 부족하다면 인출하기
            if now < days[day]:
                cnt += 1
                # 남은 돈을 집어넣고 같은 금액 재인출
                now = middle
            # 오늘 하루 소비
            now -= days[day]

        # M 번보다 많이 인출하거나, 인출액이 제일 돈이 많이 드는 하루의 소비액도 안 될 경우
        if cnt > M or middle < max(days):
            # 인출 최소 금액 증가
            minimum = middle + 1
        # 적절한 소비가 이루어진 경우
        else:
            # 인출 최대 금액 감소
            maximum = middle - 1
            # K 값 갱신
            K = middle

    return K


N, M = map(int, input().split())
days = [int(input()) for _ in range(N)]

print(binary_search(days))