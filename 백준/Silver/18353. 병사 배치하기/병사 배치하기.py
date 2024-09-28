import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 병사 배치하기 (18353)
 1. 병사를 배치할 때 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
 2. 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법 이용
[입력]
 1. N: 병사의 수
 2. 두번째 줄: 병사들의 전투력
[출력]
 1. 남아있는 병사의 수가 최대가 되도록 하기 위해서 열외해야 하는 병사의 수 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(N, soldiers):
    # 최소 값은 1
    dp = [1] * N

    # 뒤에서부터 순회
    for i in range(N - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            # 이번 값이 기준 값보다 크다면
            if soldiers[j] > soldiers[i]:
                # 이번 값은 현재 값 or 기준 값 + 1
                dp[j] = max(dp[j], dp[i] + 1)
    
    # N에서 dp 값중 가장 큰 값 빼기
    return N - max(dp)


N = int(input())
soldiers = list(map(int, input().split()))

print(dynamic_programming(N, soldiers))