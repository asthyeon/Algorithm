import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 복권(1359)
 1. 1 ~ N까지의 수 중 내가 고른 M개의 수와 판매자가 고른 M개의 수 중에서 K개 같으면 당첨
 2. 
[입력]
 1. N: 번호 수, M: 고를 수 있는 번호 수, K: 당첨 기준 수
[출력]
 1. 복권에 당첨될 확률 출력
"""

"""
<풀이>
 1. 조합 이용
"""

from itertools import combinations


# 당첨확률 구하기
def winning(chosen):
    # 당첨 수
    won = 0
    # 판매자측의 당첨번호 가정
    win_numbers = [m for m in range(1, M + 1)]
    # 내가 고른 경우의 수
    for choice in chosen:
        # 당첨된 번호 수
        k = 0
        # 판매자측의 당첨번호와 비교
        for win in win_numbers:
            if win in choice:
                k += 1
        # 당첨된 번호 수가 K보다 크거나 같으면 당첨
        if k >= K:
            won += 1

    # 당첨확률(당첨 수/전체 경우의 수)
    percent = won / len(chosen)

    return percent


# 번호 수 N, 고를 수 있는 번호 수 M, 당첨 기준 수 K
N, M, K = map(int, input().split())
numbers = [i for i in range(1, N + 1)]

# N개중 M개 고르기
chosen = list(combinations(numbers, M))

print(winning(chosen))