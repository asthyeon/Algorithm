import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이건 꼭 풀어야 해! (17390)
 1. 길이 N짜리 수열 A를 비내림차순으로 정렬
 2. Q개의 질문에 대답
  - L R: B[L] + ... + B[R]
[입력]
 1. N: 수열 A의 길이, Q: 질문의 개수
 2. 수열 A 정보
 3. Q개의 줄: L R 질문
[출력]
 1. 질문의 답을 각각 순서대로 출력
"""

"""
<풀이>
 1. 누적합
"""

# 수열 A의 길이 N, 질문의 개수 Q
N, Q = map(int, input().split())
# 수열 A
A = list(map(int, input().split()))
A.sort()

# 누적합
prefix_sum = [0] * N
for i in range(N):
    if i == 0:
        prefix_sum[i] = A[i]
    else:
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

# 질문
for _ in range(Q):
    # L ~ R 합 구하기
    L, R = map(int, input().split())

    # 변수 수정
    R = R - 1
    L = L - 2
    if L < 0:
        print(prefix_sum[R])
    else:
        print(prefix_sum[R] - prefix_sum[L])