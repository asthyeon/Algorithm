import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수들의 합 2(2003)
 1. N개의 수로 된 수열 A[1], ..., A[N]
 2. 이 수열의 i번째 수 ~ j번째 수까지의 합(A[i] + ... + A[j])가 M이 되는 경우의 수
[입력]
 1. N: 수열의 수, M: 수열의 합 목표
 2. 각 수열 정보
[출력]
 1. 경우의 수 출력
"""

"""
<풀이>
 1. 누적합 이용
"""


# 경우의 수
def number_of_cases(prefix_sum):
    outcomes = 0

    # 해당 수까지 하나씩 빼면서 M이 되는 부분 찾기
    for end in range(N + 1):
        # start ~ end
        for start in range(end):
            if prefix_sum[end] - prefix_sum[start] == M:
                outcomes += 1

    return outcomes


# 수열의 수 N, 수열의 합 목표 M
N, M = map(int, input().split())
# 수열 정보
sequence = list(map(int, input().split()))
# 누적합(첫 값이 M이 될 수 있기에 1개 더 추가)
prefix_sum = [0] * (N + 1)
for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + sequence[i - 1]

print(number_of_cases(prefix_sum))