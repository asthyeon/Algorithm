import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 호텔 (1106)
 1. 정보에 맞게 돈 투자 가능
  - 정보: "어떤 도시에서 9원을 들여서 홍보하면 3명의 고객이 늘어난다"
  - 이러한 정보에 나타난 돈에 정수배 만큼을 투자할 수 있다
[입력]
 1. C, N: 호텔이 늘려야 하는 고객 수 C, 홍보 가능 도시 수 N
 2. N개의 줄: 각 도시에 홍보할 때 드는 비용과 얻을 수 있는 고객 수
[출력]
 1. 적어도 C명 늘이기 위해 투자해야 하는 돈의 최솟값 구하기
"""

"""
<풀이>
 1. dp -> 동전문제랑 유사
 2. C명 초과로 늘이는 것이 비용이 더 적을 수도 있음
"""


# dp
def dynamic_programming(cities):
    # 최대 인원수를 인덱스로, 값을 비용으로
    dp = [10e9] * 1101
    # 제일 처음 값
    dp[0] = 0
    # 비용과 고객 수
    answer = 10e9
    for cost, customer in cities:
        for cnt in range(customer, 1101):
            # 이전 값과, 이전 배수에 비용을 더한 것중 더 작은 값
            dp[cnt] = min(dp[cnt], dp[cnt - customer] + cost)
            # C명 이상인 경우 가장 작은 값 정하기
            if C <= cnt:
                answer = min(answer, dp[cnt])

    return answer


C, N = map(int, input().split())
# 도시 리스트
cities = []
for _ in range(N):
    # 도시 홍보 비용과 고객 수
    costs, customers = map(int, input().split())

    cities.append((costs, customers))

print(dynamic_programming(cities))