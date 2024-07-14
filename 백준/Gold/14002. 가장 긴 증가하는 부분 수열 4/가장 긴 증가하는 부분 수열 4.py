import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 긴 증가하는 부분 수열 4 (14002)
 1. 수열 A가 주어졌을 때 가장 긴 증가하는 부분 수열 구하기
[입력]
 1. N: 수열 A의 크기
 2. 둘째 줄: 수열 A
[출력]
 1. 수열 A의 가장 긴 증가하는 부분 수열의 길이 출력
 2. 가장 긴 증가하는 부분 수열 출력, 수열이 여러가지인 경우 아무거나 출력
"""

"""
<풀이>
 1. dp
 2. 수열도 같이 꺼낼 방법 생각하기 -> dp 값 이용
"""


# 정답 수열 만들기
def make_sequence(maximum, dp, A):
    answer = []

    # 뒤에서부터 dp 순회
    for i in range(N - 1, -1, -1):
        # 가장 큰 길이를 줄이면서 해당하는 값 정답에 넣기
        if dp[i] == maximum:
            answer.append(A[i])
            maximum -= 1

    # 정답 오름차순 정렬
    answer.sort()
    return answer


# dp
def dynamic_programming(A):
    # 길이를 담을 리스트
    dp = [1] * N

    # 2번째 수부터 순회
    for target in range(1, N):
        # 이번 수의 이전 수들
        for previous in range(target):
            # 이번 수가 이전 수보다 크면
            if A[target] > A[previous]:
                # 길이 갱신
                dp[target] = max(dp[target], dp[previous] + 1)

    return max(dp), dp


N = int(input())
A = list(map(int, input().split()))

# 길이와 배열 받기
length, dp = dynamic_programming(A)

# 정답 출력
print(length)
print(*make_sequence(length, dp, A))
