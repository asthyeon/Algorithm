import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
[문제] LCS (9251)
1. 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것 찾기 

[풀이]
1. dp
    A C A Y K P
  0 0 0 0 0 0 0
C 0 0 1 1 1 1 1
A 0 1 1 2 2 2 2
P 0 1 1 2 2 2 3
C 0 1 2 2 2 2 3
A 0 1 2 3 3 3 3
K 0 1 2 3 3 4 4

    M W M H W C M
  0 0 0 0 0 0 0 0
C 0 0 0 0 0 0 1 1
M 0 1 1 2 2 2 2 3 -> X (이미 카운팅 된 건 처리 X)
P
O
F
V
F

    M W M H W C M
  0 0 0 0 0 0 0 0
C 0 0 0 0 0 0 1 1
M 0 1 1 1 1 1 1 2  
P
O
F
V
F
"""


def dynamic_programming(seq1, seq2):
    # 계산 편의를 위해 각 + 1
    dp = [[0] * (len(seq1) + 1) for _ in range(len(seq2) + 1)]

    for x in range(1, len(seq2) + 1):
        for y in range(1, len(seq1) + 1):
            # 문자가 같으면 대각선 + 1
            if seq1[y - 1] == seq2[x - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            # 문자가 다르면 이전 값 중 큰 값
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

    # 마지막 값 출력
    return dp[len(seq2)][len(seq1)]


seq1 = input().rstrip()
seq2 = input().rstrip()

print(dynamic_programming(seq1, seq2))