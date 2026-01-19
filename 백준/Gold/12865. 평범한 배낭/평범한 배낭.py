import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] 평범한 배낭 (12865)
1. 각 물건은 무게 W와 가치 V를 가짐
2. 해당 물건을 배낭에 넣어서 가면 V만큼 즐길 수 있음
3. 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있음

[풀이]
1. dp
2. 무게 기준
"""


def dynamic_programming(bags):
    # 최대 무게 K
    dp = [0] * (K + 1)

    # 가방 순회
    for w, v in bags:
        # 제일 큰 무게부터 해당 물건 무게까지 순회
        for i in range(K, w - 1, -1):
            # 현재 가방 무게 가치 vs 해당 물건 더한 가치
            dp[i] = max(dp[i], dp[i - w] + v)
    
    # 가방의 무게가 최대일 때 반환
    return dp[K]


N, K = map(int, input().split())
bags = []
for _ in range(N):
    W, V = map(int, input().split())
    bags.append((W, V))

print(dynamic_programming(bags))