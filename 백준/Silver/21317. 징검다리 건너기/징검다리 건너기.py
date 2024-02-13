import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 징검다리 건너기(21317)
 1. 마지막 돌에 있는 산삼 캐기
 2. 점프 3종류
  - 작은 점프: +1
  - 큰 점프: +2
  - 매우 큰 점프: +3
 3. 작은 점프와 큰 점프의 소비 에너지지는 점프를 하는 돌의 번호마다 다름 
 4. 매우 큰 점프는 단 한 번, k만큼 에너지 소비
[입력]
 1. N: 돌의 개수
 2. 1 ~ N - 1번 돌: 작점E, 큰점E
 3. K: 매큰점E
[출력]
 1. 산삼 얻는 최소 에너지
"""

"""
<풀이>
 1. dp의 냄새가 스멀스멀
0: 1 2
1: 2 3
2: 4 5
3: 6 7
4: 도착
- 매큰점 X
[0, 1, 2, 4, 7]
- 매큰점 O
[0, 1, 2, 4, 5]
 2. N번째를 뛰어넘는 경우는 고려하지 않기(산삼 뛰어넘어서 못캠)
"""


# dp
def dynamic_programming(stones):
    dp = [0] * N

    # 매큰점 X
    for i in range(1, N):
        # 첫 번째 칸은 무조건 작점
        if i == 1:
            dp[i] = stones[i - 1][0]
        # 두 번째 칸 이후로는 작점 or 큰점
        else:
            dp[i] = min(dp[i - 2] + stones[i - 2][1], dp[i - 1] + stones[i - 1][0])

    # 최소값
    answer = dp[N - 1]
    # 매큰점 O
    for j in range(3, N):
        # 안뛰는게 나은 경우 넘기기
        if dp[j] - dp[j - 3] <= K:
            continue
        # 뛰는게 나은 경우 복사본 만들고 비교
        copy = dp[:]
        copy[j] = copy[j - 3] + K
        for l in range(j + 1, N):
            copy[l] = min(copy[l - 2] + stones[l - 2][1], copy[l - 1] + stones[l - 1][0])
        answer = min(answer, copy[N - 1])

    return answer


# 돌의 개수 N
N = int(input())
# 각 돌 에너지
stones = []
for _ in range(N - 1):
    e, E = map(int, input().split())
    stones.append((e, E))
# 매큰점E K
K = int(input())

print(dynamic_programming(stones))