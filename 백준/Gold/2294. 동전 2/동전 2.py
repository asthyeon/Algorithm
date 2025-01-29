import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 동전 2
[출력: 사용한 동전의 최소 개수 출력, 불가능하면 -1 출력]
1. n가지 종류의 동전을 적당히 사용해서 그 가치의 합이 k원이 되도록 하기
2. 사용한 동전의 개수가 최소가 되어야 함
3. 가치가 같은 동전이 여러 번 주어질 수도 있음
@ 풀이
(1) dp로 풀기(동전의 수만큼 반복하여 최소값 찾기)
 - dp의 값은 동전의 최소 개수
 - dp의 인덱스 동전의 합

n = 3, k = 15
- coin이 1일 때
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- coin이 5일 때
0, 0, 0, 0, 0, 1, 0, 0, 0, 0,  2,  0,  0,  0,  0,  3
- coin이 1과, 5를 쓸 때
0, 1, 2, 3, 4, 1
dp[6] = dp[5] + dp[1] = 2
dp[7] = dp[5] + dp[2] = 3
"""


# dp 함수
def dynamic_programming(values):
    dp = [10e9] * (k + 1)

    # 0 값 설정
    dp[0] = 0

    # 동전의 수만큼 반복
    for coin in range(len(values)):
        # 같은 가치의 동전은 생략
        if coin > 0:
            if values[coin] == values[coin - 1]:
                continue
        # 해당 동전의 가치부터 반복하여 각 동전의 합에 사용된 개수 구하기
        for total in range(values[coin], k + 1):
            # 해당 값에 쓰였던 동전 개수와 해당 동전을 처음으로 사용한 개수와 비교하여 교체
            dp[total] = min(dp[total], dp[total - values[coin]] + 1)
            # print(f'{total}번째 {dp[total]}')

    # 불가능하다면 -1 출력
    if dp[k] == 10e9:
        return -1
    # 가능하다면 정답 출력
    else:
        return dp[k]


# 동전 수 n, 목표 금액 k원
n, k = map(int, input().split())
# 각 동전의 가치
values = []
for _ in range(n):
    value = int(input())
    values.append(value)

print(dynamic_programming(values))


