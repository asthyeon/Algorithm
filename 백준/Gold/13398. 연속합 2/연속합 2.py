import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 연속합 2 (13398)
 1. n개의 정수로 이루어진 임의의 수열
 2. 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합 구하기
 3. 수는 한 개 이상 선택, 수열에서 수를 하나 제거 가능(제거하지 않아도 됨)
[입력]
 1. n: 수의 개수
 2. 둘째 줄: n개의 정수로 이루어진 수열
[출력]
 1. 답 출력
"""

"""
<풀이>
 1. dp
"""


# dp
def dynamic_programming(sequence):
    # 제거하지 않은 경우와 제거한 경우
    dp1 = [0] * n
    dp2 = [0] * n
    # 첫번째 인덱스 조정
    dp1[0] = dp2[0] = sequence[0]

    # 각 구간합 순회
    for i in range(1, n):
        # 각 구간합 최대값 구하기
        dp1[i] = max(sequence[i], dp1[i - 1] + sequence[i])
        # 각 구간합에서 현재 수를 제거한 경우의 최대값
        dp2[i] = max(dp1[i - 1], dp2[i - 1] + sequence[i])

    # 두 구간 중 최대 값 반환
    return max(max(dp1), max(dp2))


n = int(input())
sequence = list(map(int, input().split()))

print(dynamic_programming(sequence))