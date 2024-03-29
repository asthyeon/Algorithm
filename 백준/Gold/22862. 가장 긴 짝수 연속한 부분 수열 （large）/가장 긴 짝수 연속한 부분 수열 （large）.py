import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 긴 짝수 연속한 부분 수열 (large)
 1. 수열 S에서 원하는 위치의 수를 골라 최대 K번 삭제 가능
[입력]
 1. N, K: 수열 S의 길이 N, 삭제 가능 최대 횟수 K
 2. 수열 S
[출력]
 1. S에서 최대 K번 삭제 후, 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이 구하기
"""

"""
<풀이>
 1. 일단 풀어보기 -> 투 포인터
 2. 예시는 다 맞는데 틀림,,
 3. 수열 안의 홀수를 세기
"""


# 투 포인터
def two_pointer(S):
    # 시작점과 끝점
    start = 0
    end = 0
    # 길이
    length = 0
    # 홀수 수
    odd = 0

    while end < N:
        # 삭제 불가능할 때 시작점 이동
        if odd > K:
            # 시작점이 홀수였다면 삭제 횟수 추가
            if S[start] % 2 == 1:
                odd -= 1
            start += 1
            continue
        # 삭제 가능할 때 끝점 이동
        else:
            # 끝점이 홀수였다면 삭제
            if S[end] % 2 == 1:
                odd += 1
            end += 1
        length = max(length, end - start - odd)

    return length


# 수열 S의 길이 N, 삭제 가능 최대 횟수 K
N, K = map(int, input().split())
# 수열 S
S = list(map(int, input().split()))

print(two_pointer(S))