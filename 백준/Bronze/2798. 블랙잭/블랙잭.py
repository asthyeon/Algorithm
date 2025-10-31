import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
<문제>
# 블랙잭 (2798)
1. 합이 M을 넘지 않는 선에서 카드 3장으로 최대 값 만들기
<풀이>
1. 브루트포스
"""


def brute_force(cards):
    answer = 0

    # 카드 하나씩 선택
    for a in cards:

        for b in cards:
            if b == a:
                continue

            for c in cards:
                if c == a or c == b:
                    continue

                # 조건을 만족한다면, 정답 교체
                tmp = a + b + c
                if tmp <= M:
                    answer = max(answer, tmp)

    return answer


# N: 카드 수, M: 최대 합
N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(brute_force(cards))