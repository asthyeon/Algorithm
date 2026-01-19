import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 안녕 (1535)
1. 세준이가 i번 사람에게 인사를 하면
 - 체력: -L[i]
 - 기쁨: +J[i]
2. 최대한의 기쁨을 얻는 방법?
3. 체력이 0 혹은 음수가 되면 죽어서 기쁨은 0

[풀이]
1. dp
2. 인사를 할 수도 안할 수도 있음
3. 체력을 기준으로 
"""


def dynamic_programming(N, L, J):
    # 체력 100 ~ 0
    dp = [0] * 101

    # 각 사람 순회
    for i in range(N):
        # 100부터 이번 사람 체력까지 역순으로
        for l in range(100, L[i], -1):
            # 현재 체력의 기쁨 vs 인사 후 체력의 기쁨
            dp[l] = max(dp[l], dp[l - L[i]] + J[i])

    # 가장 큰 값
    return max(dp)


N = int(input())
L = list(map(int, input().split()))
J = list(map(int, input().split()))

print(dynamic_programming(N, L, J))