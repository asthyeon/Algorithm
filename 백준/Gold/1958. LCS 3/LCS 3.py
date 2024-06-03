import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# LCS 3
 1. LCS = 가장 긴 공통 문자열
 2. 문자열 3개의 LCS 구하기
[입력]
 1. 각 세 줄에 문자열이 주어짐
[출력]
 1. 세 문자열의 LCS 길이 출력
"""

"""
<풀이>
 1. dp -> 3개니까 3차원
"""


def dynamic_programming(first, second, third):
    # 3차원 구현 (생성 자체는 역으로)
    dp = [[[0] * (len(third) + 1) for _ in range(len(second) + 1)] for _ in range(len(first) + 1)]

    # 이전 값을 사용해야 하므로 1부터 시작
    for f in range(1, len(first) + 1):
        for s in range(1, len(second) + 1):
            for t in range(1, len(third) + 1):
                # 세 단어가 같은 문자일 때 = 이전 값 + 1
                if first[f - 1] == second[s - 1] and second[s - 1] == third[t - 1]:
                    dp[f][s][t] = dp[f - 1][s - 1][t - 1] + 1
                # 세 문자가 다르다면 넘어온 값중 가장 큰 값으로 교체
                else:
                    dp[f][s][t] = max(dp[f - 1][s][t], dp[f][s - 1][t], dp[f][s][t - 1])

    # LCS 찾기
    answer = 0
    for f in range(len(first) + 1):
        for s in range(len(second) + 1):
            # 가장 큰 값으로 교체
            answer = max(answer, max(dp[f][s]))

    return answer


first = input().rstrip()
second = input().rstrip()
third = input().rstrip()

print(dynamic_programming(first, second, third))